from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods


@require_http_methods(['GET', 'POST']) # GET과 POST 요청만 허용 (PUT, DELETE 등은 405 에러)
def signup(request):# 회원가입
    """
    회원가입
    
    Django 내장 UserCreationForm 사용
    """
    # 이미 로그인된 상태면 메인으로
    if request.user.is_authenticated:
        # 로그인된 사용자가 회원가입 페이지에 접근하면 메인 페이지로 리다이렉트
        return redirect('games:index')
    
    if request.method == 'POST': # POST 요청이면 폼 데이터 처리
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 후 자동 로그인
            auth_login(request, user)
            return redirect('games:index')
    else:
        form = UserCreationForm() #  GET 요청이면 빈 폼 생성
    
    context = {'form': form} # 템플릿에 폼 객체 전달 (회원가입 폼)
    return render(request, 'accounts/signup.html', context) 
    # accounts/signup.html 템플릿 렌더링, context 전달


@require_http_methods(['GET', 'POST']) # GET과 POST 요청만 허용 (PUT, DELETE 등은 405 에러)
def login(request):
    """
    로그인
    
    Django 내장 AuthenticationForm 사용
    주의: 첫 인자로 request를 받음
    """
    if request.user.is_authenticated:
        return redirect('games:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        #                         ^^^^^^^ 다른 폼과 다르게 request가 첫 인자
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # next 파라미터가 있으면 해당 페이지로, 없으면 메인으로
            return redirect(request.GET.get('next') or 'games:index')
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


@require_POST
@login_required
def logout(request):
    """
    로그아웃
    
    POST 요청만 허용 (보안)
    """
    auth_logout(request)
    return redirect('games:index')
