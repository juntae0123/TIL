from django.contrib import admin
from .models import Game, Review # 같은 앱의 모델을 import (Game과 Review 모델 사용)


@admin.register(Game) # Game 모델을 관리자 사이트에 등록 (데코레이터 방식)
class GameAdmin(admin.ModelAdmin): # Game 모델의 관리자 설정 클래스 정의
    list_display = ['title', 'genre', 'release_date', 'metacritic_score', 'created_at']
    list_filter = ['genre', 'release_date']
    search_fields = ['title', 'description']
    ordering = ['-created_at']


@admin.register(Review) # Review 모델을 관리자 사이트에 등록 (데코레이터 방식)
class ReviewAdmin(admin.ModelAdmin): # Review 모델의 관리자 설정 클래스 정의
    list_display = ['game', 'author', 'rating', 'created_at']
    # 게임과 작성자보다 평점과 작성일로 필터링하는 게 더 유용할 것 같아서 list_filter 변경
    list_filter = ['rating', 'created_at'] 
    # 리뷰는 게임과 작성자보다 평점과 작성일로 필터링하는 게 더 유용할 것 같아서 변경
    search_fields = ['content'] # 리뷰 내용 검색 가능
    ordering = ['-created_at'] # 리뷰도 생성일 내림차순으로 정렬
