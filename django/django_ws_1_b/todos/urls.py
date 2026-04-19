# todos 앱 내부의 세부 주소 설정
from django.urls import path
from . import views

urlpatterns = [
    # 주소가 빈 문자열('')이면 views.py의 index 함수를 실행
    # 실제 주소: /todos/
    path('', views.index, name='index'),
    
    # 주소가 'create/'이면 views.py의 create 함수를 실행
    # 실제 주소: /todos/create/
    path('create/', views.create, name='create'),
]