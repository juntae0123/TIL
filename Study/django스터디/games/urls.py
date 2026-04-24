from django.urls import path # URL 패턴을 정의하기 위한 함수
from . import views

app_name = 'games'

urlpatterns = [
    # 게임 CRUD
    path('', views.index, name='index'), # 게임 목록 페이지 (READ - List)
    path('create/', views.create, name='create'), # 게임 등록 페이지 (CREATE)
    path('<int:pk>/', views.detail, name='detail'), # 게임 상세 페이지 (READ - Detail)
    path('<int:pk>/update/', views.update, name='update'), # 게임 수정 페이지 (UPDATE)
    path('<int:pk>/delete/', views.delete, name='delete'), # 게임 삭제 (DELETE)
    
    # 리뷰 (게임에 종속)
    path('<int:game_pk>/reviews/create/', views.review_create, name='review_create'),
    path('<int:game_pk>/reviews/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
] # URL 패턴 리스트 (게임 CRUD와 리뷰 관련 URL 포함)
