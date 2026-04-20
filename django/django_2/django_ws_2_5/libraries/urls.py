from django.urls import path
from . import views

app_name = 'libraries' # url 태그 사용을 위한 네임스페이스

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/', views.recommend, name='recommend'),
    path('bestseller/', views.bestseller, name='bestseller'),
]