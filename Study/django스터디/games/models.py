from django.db import models # Django의 모델 시스템을 사용하기 위해 import
from django.conf import settings # settings에서 AUTH_USER_MODEL을 참조하기 위해 import


class Game(models.Model):
    """
    게임 정보 모델
    
    필드 옵션 설명:
    - CharField/TextField: blank=True만 사용 (빈 문자열로 저장)
    - IntegerField/DateField: null=True, blank=True 둘 다 사용 (NULL로 저장)
    - ImageField: blank=True만 사용 (파일 경로가 문자열이라서)
    """
    
    # 필수 필드
    title = models.CharField(max_length=200) # 게임 제목 (최대 200자)
    genre = models.CharField(max_length=100) # 게임 장르 (최대 100자)
    
    # 선택 필드 (문자열)
    description = models.TextField(blank=True) # 게임 설명 (빈 문자열 허용)
    
    # 선택 필드 (비문자열)
    release_date = models.DateField(null=True, blank=True) # 발매일 (NULL 허용)
    metacritic_score = models.IntegerField(null=True, blank=True) # 메타크리틱 점수 (NULL 허용)
    
    # 이미지 필드
    cover_image = models.ImageField( # 이미지 업로드 필드
        upload_to='games/covers/', # 업로드된 이미지가 저장될 경로
        blank=True, # 빈 문자열 허용 (이미지 업로드는 선택 사항)
    )
    
    # 자동 타임스탬프
    created_at = models.DateTimeField(auto_now_add=True) # 생성 시 자동으로 현재 시간 저장
    updated_at = models.DateTimeField(auto_now=True) # 저장 시마다 현재 시간으로 업데이트
    
    class Meta:
        ordering = ['-created_at'] # 기본 정렬 순서: 생성일 내림차순
    
    def __str__(self):
        return self.title # 객체를 문자열로 표현할 때 게임 제목을 반환


class Review(models.Model): 
    """
    게임 리뷰 모델
    
    Game과 User에 대한 FK를 가짐
    - on_delete=CASCADE: 부모 삭제 시 함께 삭제
    - related_name: 역참조 시 사용 (game.reviews.all())
    """
    
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    
    # 외래키 (필수 관계) 
    game = models.ForeignKey( # Game 모델과의 외래키
        Game,
        on_delete=models.CASCADE, # 게임이 삭제되면 해당 리뷰도 삭제
        related_name='reviews', # 역참조 시 game.reviews.all()로 해당 게임의 모든 리뷰에 접근 가능
    )
    author = models.ForeignKey( # User 모델과의 외래키
        settings.AUTH_USER_MODEL, # Django의 기본 User 모델을 참조
        on_delete=models.CASCADE, # 사용자가 삭제되면 해당 리뷰도 삭제
        related_name='reviews', # 역참조 시 user.reviews.all()로 해당 사용자의 모든 리뷰에 접근 가능
    )
    
    # 리뷰 내용
    rating = models.IntegerField(choices=RATING_CHOICES) # 평점 (1~5, 선택지로 제한)
    content = models.TextField() # 리뷰 내용 (필수)
    playtime_hours = models.IntegerField(null=True, blank=True) # 플레이 시간 (NULL 허용)
    
    # 자동 타임스탬프
    created_at = models.DateTimeField(auto_now_add=True) # 생성 시 자동으로 현재 시간 저장
    updated_at = models.DateTimeField(auto_now=True) # 저장 시마다 현재 시간으로 업데이트
    
    class Meta:
        ordering = ['-created_at'] # 기본 정렬 순서: 생성일 내림차순
    
    def __str__(self):
        return f'{self.author.username}의 {self.game.title} 리뷰' # 객체를 문자열로 표현할 때 "작성자 이름의 게임 제목 리뷰" 형식으로 반환
