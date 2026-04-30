# =============================================================================
# models.py
# 역할: Django ORM 데이터베이스 스키마 정의
# 원리: CrawlResult 모델 하나에 종목명, 원본/정제/증강 댓글(JSONField),
#       IQR 임계값, 요약문, 생성 일시를 저장한다.
#       댓글 목록은 JSON 배열로 단일 테이블에 저장하여 조회를 단순화한다.
# =============================================================================

from django.db import models


class CrawlResult(models.Model):
    """토스증권 커뮤니티 크롤링 결과를 저장하는 모델"""

    # 실제 종목명 (검색어와 다를 수 있음 – 토스증권이 반환하는 종목명 저장)
    stock_name = models.CharField(max_length=100, verbose_name="실제 종목명")

    # 원본 댓글 목록: ["댓글1", "댓글2", ...] 형태의 JSON 배열
    raw_comments = models.JSONField(default=list, verbose_name="원본 댓글 목록")

    # 정제 댓글 목록: 길이 필터링 + 특수문자 제거 + 부적절 댓글 제거 후 결과
    cleaned_comments = models.JSONField(default=list, verbose_name="정제 댓글 목록")

    # 증강 댓글 목록: OpenAI API로 의미 보존 확장 생성된 댓글
    augmented_comments = models.JSONField(default=list, verbose_name="증강 댓글 목록")

    # IQR 임계값 정보: "Q1=XX, Q3=YY, lower=AA, upper=BB" 형태 문자열
    iqr_info = models.CharField(max_length=255, blank=True, verbose_name="IQR 임계값 정보")

    # 전체 동향 요약문 (F110)
    summary = models.TextField(blank=True, verbose_name="전체 동향 요약")

    # 레코드 생성 일시 (자동 기록)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "크롤링 결과"
        verbose_name_plural = "크롤링 결과 목록"

    def __str__(self):
        return f"{self.stock_name} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
