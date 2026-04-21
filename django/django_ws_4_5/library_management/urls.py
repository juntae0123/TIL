# [library_management/urls.py]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # libraries 앱의 urls.py 파일을 연결
    path('libraries/', include('libraries.urls')),
]