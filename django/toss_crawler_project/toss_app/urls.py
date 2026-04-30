# =============================================================================
# toss_app/urls.py
# 역할: 앱 수준 URL 라우팅 정의
# 원리: Django URL dispatcher가 요청 경로를 views의 함수/클래스에 매핑한다.
#       메인(입력) 페이지와 결과 조회 페이지 두 엔드포인트를 제공한다.
# =============================================================================

from django.urls import path
from . import views

app_name = "toss_app"

urlpatterns = [
    # 메인 입력 폼 (GET: 폼 렌더링 / POST: 크롤링 실행)
    path("", views.index, name="index"),

    # 결과 페이지 (크롤링 완료 후 DB pk 기반 조회)
    path("result/<int:pk>/", views.result, name="result"),
]
