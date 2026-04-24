from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm
from .models import Post

# --- views.py ---
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user) # F502: 가입 완료 시 자동 로그인
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def post_create_view(request):
    # F506: 게시글 작성 (현재 로그인 유저 자동 할당)
    if request.method == 'POST':
        Post.objects.create(
            author=request.user,
            title=request.POST.get('title'),
            content=request.POST.get('content')
        )
        return redirect('main')
    return render(request, 'posts/post_form.html')

@login_required
def post_update_view(request, post_id):
    # F506: 게시글 수정 (권한 검증 포함)
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect('main')
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('main')
    return render(request, 'posts/post_form.html', {'post': post})

@login_required
def post_delete_view(request, post_id):
    # F506: 게시글 삭제 (권한 검증 포함)
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        post.delete()
    else:
        messages.error(request, "삭제 권한이 없습니다.")
    return redirect('main')

@login_required
def profile_view(request):
    # F507: 프로필 페이지 (역참조를 통한 데이터 전달)
    context = {
        'user_posts': request.user.posts.all(),
        'interest_stocks': request.user.interest_stocks.all(),
    }
    return render(request, 'accounts/profile.html', context)