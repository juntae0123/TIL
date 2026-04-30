# =============================================================================
# toss_app/services/llm_processor.py
# 역할: 댓글 전처리(F105) · 데이터 증강(F106) · 동향 요약(F110)
# 원리:
#   [전처리]
#     1. 길이 필터링: IQR(사분위 범위)로 이상치 길이 제거 – numpy 없이 순수 Python으로 구현
#     2. 정규표현식: re 모듈로 특수문자·이모지·URL·반복 패턴 제거
#     3. OpenAI API: 부적절 댓글(욕설·혐오) 일괄 판별 후 제거
#   [증강]
#     OpenAI API로 정제된 댓글마다 원래 의미를 유지한 다른 표현 생성
#   [요약]
#     정제 댓글 전체를 프롬프트에 넣어 전체 투자 동향 요약 생성
# =============================================================================

import re
import logging
import os
import json

from openai import OpenAI

logger = logging.getLogger(__name__)

# ── OpenAI 설정 ──────────────────────────────────────────────────────────────
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4o-mini"  # 비용 효율적인 모델 사용

# ── 전처리 파라미터 ──────────────────────────────────────────────────────────
MIN_LEN = 5      # 최소 댓글 길이 (문자 수)
MAX_LEN = 300    # 최대 댓글 길이 (문자 수)


class LLMProcessor:
    """댓글 전처리, 증강, 요약을 담당하는 서비스 클래스."""

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    # =========================================================================
    # 공개 API
    # =========================================================================

    def preprocess(self, raw_comments: list[str]) -> tuple[list[str], str]:
        """
        원본 댓글 리스트를 전처리하여 정제 목록과 IQR 정보를 반환한다.

        Returns:
            (정제된 댓글 리스트, IQR 정보 문자열)
        """
        # Step 1: 기본 길이 필터 (MIN_LEN / MAX_LEN 하드 컷)
        after_hard_cut = [c for c in raw_comments if MIN_LEN <= len(c) <= MAX_LEN]
        logger.info("Hard cut: %d → %d", len(raw_comments), len(after_hard_cut))

        # Step 2: IQR 기반 이상치 길이 제거
        after_iqr, iqr_info = self._filter_by_iqr(after_hard_cut)
        logger.info("IQR filter: %d → %d  [%s]", len(after_hard_cut), len(after_iqr), iqr_info)

        # Step 3: 정규표현식 정제
        after_regex = [self._clean_text(c) for c in after_iqr]
        after_regex = [c for c in after_regex if len(c) >= MIN_LEN]
        logger.info("Regex clean: %d → %d", len(after_iqr), len(after_regex))

        # Step 4: OpenAI 기반 부적절 댓글 필터링
        cleaned = self._filter_inappropriate(after_regex)
        logger.info("LLM filter: %d → %d", len(after_regex), len(cleaned))

        return cleaned, iqr_info

    def augment(self, cleaned_comments: list[str]) -> list[str]:
        """
        정제 댓글 리스트를 입력받아 의미 보존 확장 텍스트를 생성한다.
        API 비용 절감을 위해 배치(최대 10개)로 한 번에 처리한다.
        """
        if not cleaned_comments:
            return []

        augmented = []
        batch_size = 10

        for i in range(0, len(cleaned_comments), batch_size):
            batch = cleaned_comments[i: i + batch_size]
            batch_result = self._augment_batch(batch)
            augmented.extend(batch_result)

        logger.info("Augmented %d comments", len(augmented))
        return augmented

    def summarize(self, cleaned_comments: list[str]) -> str:
        """
        정제 댓글 전체를 바탕으로 투자 동향 요약문을 생성한다 (F110).
        """
        if not cleaned_comments:
            return "분석할 댓글이 없습니다."

        joined = "\n".join(f"- {c}" for c in cleaned_comments)
        prompt = (
            "아래는 특정 주식 종목의 투자자 커뮤니티 댓글 목록입니다.\n"
            "댓글들을 종합하여 투자자들의 전체적인 시장 심리와 주요 관심사를 "
            "3~5문장으로 요약해 주세요. 중립적이고 객관적인 어조를 유지하세요.\n\n"
            f"{joined}"
        )

        try:
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300,
                temperature=0.4,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error("Summarize API error: %s", e)
            return "요약 생성 중 오류가 발생했습니다."

    # =========================================================================
    # 내부 메서드: IQR 필터링
    # =========================================================================

    def _filter_by_iqr(self, comments: list[str]) -> tuple[list[str], str]:
        """
        댓글 길이의 IQR을 계산하여 이상치를 제거한다.
        IQR = Q3 - Q1, 정상 범위: [Q1 - 1.5*IQR, Q3 + 1.5*IQR]
        """
        if len(comments) < 4:
            return comments, "데이터 부족으로 IQR 미적용"

        lengths = sorted(len(c) for c in comments)
        n = len(lengths)

        q1 = self._percentile(lengths, 25)
        q3 = self._percentile(lengths, 75)
        iqr = q3 - q1
        lower = max(MIN_LEN, q1 - 1.5 * iqr)
        upper = min(MAX_LEN, q3 + 1.5 * iqr)

        filtered = [c for c in comments if lower <= len(c) <= upper]
        iqr_info = (
            f"Q1={q1:.1f}, Q3={q3:.1f}, IQR={iqr:.1f}, "
            f"lower={lower:.1f}, upper={upper:.1f}"
        )
        return filtered, iqr_info

    @staticmethod
    def _percentile(sorted_data: list, p: float) -> float:
        """순수 Python으로 백분위수 계산 (numpy 불필요)."""
        n = len(sorted_data)
        idx = (p / 100) * (n - 1)
        lo = int(idx)
        hi = lo + 1
        if hi >= n:
            return float(sorted_data[-1])
        frac = idx - lo
        return sorted_data[lo] * (1 - frac) + sorted_data[hi] * frac

    # =========================================================================
    # 내부 메서드: 정규표현식 정제
    # =========================================================================

    @staticmethod
    def _clean_text(text: str) -> str:
        """
        re 모듈로 텍스트를 단계적으로 정제한다.
        1. URL 제거
        2. 이모지·특수기호 제거
        3. 해시태그·멘션 제거
        4. 반복 문자 축약 (ㅋㅋㅋㅋ → ㅋ)
        5. 과도한 공백 정리
        """
        # URL 제거
        text = re.sub(r"https?://\S+|www\.\S+", "", text)

        # 이모지 제거 (유니코드 이모지 범위)
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"
            "\U0001F300-\U0001F5FF"
            "\U0001F680-\U0001F6FF"
            "\U0001F1E0-\U0001F1FF"
            "\U00002700-\U000027BF"
            "\U000024C2-\U0001F251"
            "]+",
            flags=re.UNICODE,
        )
        text = emoji_pattern.sub("", text)

        # 해시태그·멘션 제거
        text = re.sub(r"[#@]\S+", "", text)

        # 특수문자 제거 (한글·영어·숫자·기본 문장부호 유지)
        text = re.sub(r"[^\w\s가-힣a-zA-Z0-9.,!?%\-]", " ", text)

        # 반복 자모 축약: ㅋㅋㅋ→ㅋ, ㅎㅎㅎ→ㅎ, ㅠㅠ→ㅠ 등
        text = re.sub(r"([ㄱ-ㅎㅏ-ㅣ])\1{2,}", r"\1", text)

        # 반복 단어 패턴 축약 (예: "좋아 좋아 좋아" → "좋아")
        text = re.sub(r"\b(\S+)( \1){2,}\b", r"\1", text)

        # 과도한 공백 정리
        text = re.sub(r"\s+", " ", text).strip()

        return text

    # =========================================================================
    # 내부 메서드: OpenAI 기반 부적절 댓글 필터링
    # =========================================================================

    def _filter_inappropriate(self, comments: list[str]) -> list[str]:
        """
        OpenAI API에 댓글 목록을 보내 부적절한 댓글(욕설·혐오·스팸)의
        인덱스를 식별하고 제거한다.
        응답은 JSON 배열(제거할 인덱스 목록) 형태를 요청한다.
        """
        if not comments:
            return []

        numbered = "\n".join(f"[{i}] {c}" for i, c in enumerate(comments))
        prompt = (
            "아래는 주식 커뮤니티 댓글 목록입니다. "
            "욕설, 혐오표현, 스팸, 광고, 개인정보가 포함된 댓글의 번호를 "
            "JSON 배열로만 응답하세요. 문제없는 댓글이라면 빈 배열 []을 반환하세요.\n"
            "예시 응답: [0, 3, 7]\n\n"
            f"{numbered}"
        )

        try:
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0,
            )
            raw = response.choices[0].message.content.strip()
            # JSON 파싱: 응답에서 배열만 추출
            match = re.search(r"\[.*?\]", raw, re.DOTALL)
            bad_indices = set(json.loads(match.group())) if match else set()
            logger.info("LLM flagged indices: %s", bad_indices)
        except Exception as e:
            logger.error("Filter API error (skipping filter): %s", e)
            bad_indices = set()

        return [c for i, c in enumerate(comments) if i not in bad_indices]

    # =========================================================================
    # 내부 메서드: 배치 증강
    # =========================================================================

    def _augment_batch(self, comments: list[str]) -> list[str]:
        """
        댓글 배치를 OpenAI API에 보내 각 댓글에 대한 의미 보존 확장 텍스트를 생성한다.
        응답은 JSON 배열로 요청하여 파싱 안정성을 높인다.
        """
        numbered = "\n".join(f"[{i}] {c}" for i, c in enumerate(comments))
        prompt = (
            "아래는 주식 투자자 커뮤니티 댓글 목록입니다. "
            "각 댓글의 핵심 의미와 감성(긍정/부정/중립)을 유지하면서 "
            "다른 어휘와 표현으로 자연스럽게 재작성하세요. "
            "JSON 배열 형태로만 응답하며, 원본과 동일한 순서로 반환하세요.\n"
            "예시: [\"재작성된 댓글0\", \"재작성된 댓글1\"]\n\n"
            f"{numbered}"
        )

        try:
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,
                temperature=0.7,
            )
            raw = response.choices[0].message.content.strip()
            match = re.search(r"\[.*?\]", raw, re.DOTALL)
            if match:
                augmented = json.loads(match.group())
                # 길이 보정: API 응답 개수가 다를 경우 원본으로 채움
                if len(augmented) < len(comments):
                    augmented.extend(comments[len(augmented):])
                return [str(a) for a in augmented[: len(comments)]]
        except Exception as e:
            logger.error("Augment API error: %s", e)

        # 실패 시 원본 반환
        return comments
