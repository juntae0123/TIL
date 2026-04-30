# =============================================================================
# toss_project/urls.py
# 역할: 프로젝트 수준 URL 라우팅 – toss_app URL을 루트에 포함
# =============================================================================

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("toss_app.urls", namespace="toss_app")),
]
