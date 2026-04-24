# [Models & Forms] F501, F502: 커스텀 유저, 관심 종목, 게시글 모델 및 회원가입 폼 정의
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

# --- models.py ---
class Stock(models.Model):
    # 관심 종목 관리를 위한 독립 모델 (데이터 정규화)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    # 요구사항 F501 반영 커스텀 유저 모델
    nickname = models.CharField(max_length=50, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    interest_stocks = models.ManyToManyField(Stock, blank=True, related_name='interested_users')

class Post(models.Model):
    # 요구사항 F506 반영 작성자 추적용 ForeignKey 설정
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)