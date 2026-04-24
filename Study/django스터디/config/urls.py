"""
URL configuration for gamelog project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # 관리자 페이지 URL
    path('', include('games.urls')), # games 앱의 URL을 포함
    path('accounts/', include('accounts.urls')), # accounts 앱의 URL을 포함
]

# 개발 환경에서 미디어 파일 서빙
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    # 미디어 파일 URL 패턴 추가
