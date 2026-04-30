# =============================================================================
# toss_app/views.py
# 역할: HTTP 요청 처리 및 서비스 레이어 오케스트레이션
# 원리: 비즈니스 로직(크롤링·전처리·증강)은 services/ 모듈에 위임하고,
#       views.py는 요청 수신 → 서비스 호출 → 렌더링/리다이렉트만 담당한다.
#       POST 처리 후 PRG(Post-Redirect-Get) 패턴으로 새로고침 중복 제출을 방지한다.
# =============================================================================

import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import CrawlResult
from .forms import SearchForm
from .services.crawler import TossCrawler
from .services.llm_processor import LLMProcessor

logger = logging.getLogger(__name__)


def index(request):
    """
    GET : 회사명 입력 폼 렌더링
    POST: 크롤링 파이프라인 실행 후 결과 페이지로 리다이렉트
    """
    form = SearchForm()

    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data["company_name"]

            try:
                # ── 1. 크롤링 ──────────────────────────────────────────────
                crawler = TossCrawler()
                stock_name, raw_comments = crawler.crawl(company_name)

                if not raw_comments:
                    messages.warning(
                        request,
                        f"'{company_name}'의 커뮤니티 댓글을 찾을 수 없습니다. "
                        "종목명을 확인하거나 잠시 후 다시 시도해 주세요.",
                    )
                    return render(request, "index.html", {"form": form})

                # ── 2. 전처리 + 증강 + 요약 ────────────────────────────────
                processor = LLMProcessor()
                cleaned, iqr_info = processor.preprocess(raw_comments)

                if not cleaned:
                    messages.warning(
                        request,
                        "전처리 후 유효한 댓글이 남지 않았습니다. "
                        "다른 종목을 시도해 주세요.",
                    )
                    return render(request, "index.html", {"form": form})

                augmented = processor.augment(cleaned)
                summary = processor.summarize(cleaned)

                # ── 3. DB 저장 ─────────────────────────────────────────────
                result_obj = CrawlResult.objects.create(
                    stock_name=stock_name,
                    raw_comments=raw_comments,
                    cleaned_comments=cleaned,
                    augmented_comments=augmented,
                    iqr_info=iqr_info,
                    summary=summary,
                )

                # PRG 패턴: POST 완료 후 결과 페이지로 리다이렉트
                return redirect("toss_app:result", pk=result_obj.pk)

            except ValueError as e:
                # F111: 검색 결과 없음 등 예상된 예외
                messages.error(request, str(e))
                logger.warning("ValueError during crawl: %s", e)

            except Exception as e:
                messages.error(
                    request,
                    "처리 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.",
                )
                logger.exception("Unexpected error during crawl pipeline: %s", e)

    return render(request, "index.html", {"form": form})


def result(request, pk):
    """
    GET: DB에 저장된 크롤링 결과를 조회하여 result.html 렌더링
    """
    obj = get_object_or_404(CrawlResult, pk=pk)
    context = {
        "obj": obj,
        "raw_count": len(obj.raw_comments),
        "cleaned_count": len(obj.cleaned_comments),
        "augmented_count": len(obj.augmented_comments),
    }
    return render(request, "result.html", context)
