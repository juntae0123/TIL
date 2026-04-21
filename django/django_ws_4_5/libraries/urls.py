# [libraries/urls.py]
from django.urls import path
from . import views

app_name = 'libraries'

urlpatterns = [
    # http://127.0.0.1:8000/libraries/ 접속 시 index 함수 실행
    path('', views.index, name='index'),
]