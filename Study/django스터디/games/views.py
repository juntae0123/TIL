from django.shortcuts import render, redirect, get_object_or_404 
# render: 템플릿 렌더링, redirect: URL 리다이렉트, get_object_or_404: 객체 조회 실패 시 404 에러
from django.contrib.auth.decorators import login_required
# 로그인 필요 데코레이터 (뷰에 적용 시 로그인한 사용자만 접근 가능)
from django.views.decorators.http import require_POST, require_http_methods
# HTTP 메서드 제한 데코레이터 (POST, GET/POST 등)
from .models import Game, Review
# 같은 앱의 모델을 import (Game과 Review 모델 사용)
from .forms import GameForm, ReviewForm
# 같은 앱의 폼을 import (GameForm과 ReviewForm 사용)

# ============================================================
# 게임 목록 (READ - List)
# ============================================================
def index(request):
    """
    모든 게임 목록 표시
    
    render(request, template, context)
    - context: 템플릿에 전달할 데이터 딕셔너리
    """
    games = Game.objects.all() # 모든 게임 객체 조회 (쿼리셋)
    context = {
        'games': games, # 템플릿에서 {{ games }}로 접근 가능 (게임 목록)
    }
    return render(request, 'games/index.html', context) 
    # games/index.html 템플릿 렌더링, context 전달


# ============================================================
# 게임 상세 (READ - Detail)
# ============================================================
def detail(request, pk): 
    # URL에서 전달받은 게임 ID(pk)를 사용하여 특정 게임의 상세 정보와 리뷰 목록을 표시
    """
    특정 게임의 상세 정보와 리뷰 목록 표시
    
    pk: URL에서 전달받은 게임 ID
    get_object_or_404: 객체 없으면 404 에러 반환
    """
    game = get_object_or_404(Game, pk=pk) # pk에 해당하는 Game 객체 조회, 없으면 404 에러
    reviews = game.reviews.all()  # related_name='reviews' 활용
    review_form = ReviewForm()  # 리뷰 작성 폼
    
    context = {
        'game': game,              # 템플릿에서 {{ game }}로 접근 가능 (게임 객체)
        'reviews': reviews,        # 템플릿에서 {{ reviews }}로 접근 가능 (게임에 달린 리뷰 목록)
        'review_form': review_form,# 리뷰 작성 폼도 템플릿에 전달 (게임 상세 페이지에서 리뷰 작성 가능)
    }
    return render(request, 'games/detail.html', context) 
    # games/detail.html 템플릿 렌더링, context 전달


# ============================================================
# 게임 생성 (CREATE)
# ============================================================
@login_required
@require_http_methods(['GET', 'POST']) # GET과 POST 요청만 허용 (PUT, DELETE 등은 405 에러)
def create(request):
    """
    게임 등록
    
    GET: 빈 폼 표시
    POST: 데이터 저장
    
    주의: 파일 업로드 시 request.FILES 필수
    """
    if request.method == 'POST': 
        # POST: 데이터 바인딩
        form = GameForm(request.POST, request.FILES)
        #                             ^^^^^^^^^^^ 파일 데이터 포함!
        if form.is_valid():
            game = form.save() # 유효성 검사 통과 시 DB에 저장 (INSERT 쿼리)
            return redirect('games:detail', pk=game.pk)
        # 유효성 검사 실패 시 form에 에러 메시지가 포함된 상태로 다시 렌더링
    else:
        # GET: 빈 폼
        form = GameForm() # 빈 폼 인스턴스 생성 (초기값 없음)
    
    context = {'form': form}
    return render(request, 'games/create.html', context)
    # games/create.html 템플릿 렌더링, context 전달 (폼 객체)


# ============================================================
# 게임 수정 (UPDATE)
# ============================================================
@login_required # 로그인한 사용자만 접근 가능
@require_http_methods(['GET', 'POST']) # GET과 POST 요청만 허용 (PUT, DELETE 등은 405 에러)
def update(request, pk):
    """
    게임 정보 수정
    
    핵심: instance 인자
    - instance 있으면 → UPDATE 쿼리
    - instance 없으면 → INSERT 쿼리 (새 레코드 생성)
    """
    game = get_object_or_404(Game, pk=pk) # pk에 해당하는 Game 객체 조회, 없으면 404 에러
    
    if request.method == 'POST':
        # POST + instance: 기존 객체 수정
        form = GameForm(request.POST, request.FILES, instance=game)
        #                                            ^^^^^^^^^^^^^ 필수!
        if form.is_valid(): # 유효성 검사 통과 시 DB에 저장 (UPDATE 쿼리)
            form.save()  # UPDATE 쿼리 실행
            return redirect('games:detail', pk=game.pk) # 수정 완료 후 상세 페이지로 리다이렉트
    else:
        # GET + instance: 기존 데이터로 폼 채우기
        form = GameForm(instance=game) 
        # instance=game → 폼이 game 객체의 데이터를 초기값으로 사용 (수정 폼)
    
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'games/update.html', context)
    # games/update.html 템플릿 렌더링, context 전달 (폼 객체와 게임 객체)


# ============================================================
# 게임 삭제 (DELETE)
# ============================================================
@login_required # 로그인한 사용자만 접근 가능
@require_POST  # POST 요청만 허용 (GET 삭제 방지)
def delete(request, pk):
    """
    게임 삭제
    
    @require_POST: GET 요청 시 405 에러 반환
    → CSRF 공격 방어
    """
    game = get_object_or_404(Game, pk=pk) # pk에 해당하는 Game 객체 조회, 없으면 404 에러
    game.delete() # 객체 삭제 (DELETE 쿼리 실행)
    return redirect('games:index') # 삭제 완료 후 게임 목록 페이지로 리다이렉트


# ============================================================
# 리뷰 생성 (중첩 리소스)
# ============================================================
@login_required
@require_POST
def review_create(request, game_pk):
    """
    특정 게임에 리뷰 작성
    
    핵심: commit=False
    - Form에 없는 필드(game, author)를 직접 할당
    - commit=False 없이 save() 시 IntegrityError 발생
    """
    game = get_object_or_404(Game, pk=game_pk)
    form = ReviewForm(request.POST)
    
    if form.is_valid():
        # commit=False: DB 저장 지연
        review = form.save(commit=False)
        
        # FK 직접 할당
        review.game = game
        review.author = request.user
        
        # 이제 DB에 저장
        review.save()
    
    return redirect('games:detail', pk=game_pk)


# ============================================================
# 리뷰 삭제
# ============================================================
@login_required
@require_POST
def review_delete(request, game_pk, review_pk):
    """
    리뷰 삭제 (본인만 가능)
    """
    review = get_object_or_404(Review, pk=review_pk)
    
    # 권한 체크: 작성자만 삭제 가능
    if request.user == review.author:
        review.delete()
    
    return redirect('games:detail', pk=game_pk)
