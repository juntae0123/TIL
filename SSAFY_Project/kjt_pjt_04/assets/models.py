# assets/models.py
# [F402] 게시글(Post) 데이터베이스 모델 정의
# 명세서 기준 제약조건(길이 제한, 기본값, 날짜 자동 갱신) 반영

from django.db import models


class Post(models.Model):
    asset_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, default="익명", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.author or not self.author.strip():
            self.author = "익명"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.asset_id})"
