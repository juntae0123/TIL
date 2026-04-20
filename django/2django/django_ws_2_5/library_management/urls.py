from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 요구사항: 127.0.0.1:8000/libraries/ 로 시작하도록 설정
    path('libraries/', include('libraries.urls')),
]