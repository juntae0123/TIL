# libraries_management/urls.py
from django.contrib import admin
from django.urls import path, include  # 1. include가 반드시 있어야 합니다!

urlpatterns = [
    path('admin/', admin.site.urls),  # 2. admin.site.register가 아니라 .urls입니다.
    # 3. 아래 줄이 누락되었거나 오타가 있으면 libraries/ 경로를 못 찾습니다.
    path('libraries/', include('libraries.urls')), 
]