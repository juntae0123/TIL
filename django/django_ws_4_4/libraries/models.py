# [libraries/models.py]
# 알라딘 API 정보를 내 DB에 저장하기 위한 설계도
from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=20, unique=True) # 중복 저장 방지를 위해 unique 설정
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateField()
    price_sales = models.IntegerField()  # 판매가
    description = models.TextField()     # 요약
    publisher = models.CharField(max_length=100) # 출판사
    customer_review_rank = models.IntegerField() # 고객 평점
    
    def __str__(self):
        return self.title