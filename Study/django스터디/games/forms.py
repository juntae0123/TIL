from django import forms # Django의 폼 라이브러리를 import
from .models import Game, Review # 같은 앱의 모델을 import (Game과 Review 모델 사용)


class GameForm(forms.ModelForm): #  Game 모델을 기반으로 하는 폼 클래스 정의
    """
    게임 등록/수정 폼
    
    ModelForm은 Model을 기반으로 폼 필드를 자동 생성
    """
    
    class Meta:
        model = Game # 이 폼이 사용할 모델 지정
        fields = [ # 폼에 포함할 모델 필드 목록
            'title', 
            'genre', 
            'description', 
            'release_date', 
            'metacritic_score', 
            'cover_image',
        ]
        
        widgets = { # 각 필드에 사용할 HTML 위젯과 속성 정의
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '게임 제목을 입력하세요',
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '예: 액션 RPG, 어드벤처',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': '게임에 대한 설명을 입력하세요',
            }),
            'release_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'metacritic_score': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 100,
                'placeholder': '0-100 사이 점수',
            }),
            'cover_image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
        
        labels = { # 각 필드에 대한 레이블 정의
            'title': '게임 제목',
            'genre': '장르',
            'description': '설명',
            'release_date': '출시일',
            'metacritic_score': '메타크리틱 점수',
            'cover_image': '커버 이미지',
        }


class ReviewForm(forms.ModelForm): # Review 모델을 기반으로 하는 폼 클래스 정의
    """
    리뷰 작성 폼
    
    game, author 필드는 포함하지 않음
    → View에서 직접 할당 (commit=False 활용)
    """
    
    class Meta:
        model = Review # 이 폼이 사용할 모델 지정
        fields = ['rating', 'content', 'playtime_hours'] # 폼에 포함할 모델 필드 목록 (game, author는 제외)
        
        widgets = {
            'rating': forms.Select(attrs={ # 평점은 드롭다운 선택으로 제공
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={ # 리뷰 내용은 텍스트 영역으로 제공
                'class': 'form-control',
                'rows': 4,
                'placeholder': '게임에 대한 솔직한 리뷰를 작성해주세요',
            }),
            'playtime_hours': forms.NumberInput(attrs={ # 플레이 시간은 숫자 입력으로 제공
                'class': 'form-control',
                'min': 0,
                'placeholder': '플레이 시간 (시간 단위)',
            }),
        }
        
        labels = {
            'rating': '별점',
            'content': '리뷰 내용',
            'playtime_hours': '플레이 시간',
        }
