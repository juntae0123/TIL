from django.urls import path
from . import views

app_name = 'accounts' # URL 네임스페이스 설정 (accounts:signup, accounts:login, accounts:logout)

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # 회원가입 페이지 URL (accounts/signup/), views.signup 뷰 함수와 연결, URL 이름은 'signup'
    path('login/', views.login, name='login'),
    # 로그인 페이지 URL (accounts/login/), views.login 뷰 함수와 연결, URL 이름은 'login'
    path('logout/', views.logout, name='logout'),
    # 로그아웃 URL (accounts/logout/), views.logout 뷰 함수와 연결, URL 이름은 'logout'
]
