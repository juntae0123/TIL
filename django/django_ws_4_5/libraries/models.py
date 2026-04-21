# libraries/models.py
from django.db import models
import requests

class Book(models.Model):
    # [필드 정의] 요구사항: 최소 8개 필드, isbn/제목/발행일 포함
    isbn = models.CharField(max_length=10)        # ISBN (10자리 제한)
    author = models.TextField()                  # 저자
    title = models.TextField()                   # 제목
    category_name = models.TextField()           # 카테고리명
    category_id = models.IntegerField()          # 카테고리 ID
    price = models.IntegerField()                # 판매가
    fixed_price = models.BooleanField()          # 정찰제 여부
    pub_date = models.DateField()                # 발행일

    def __str__(self):
        # 관리자 페이지에서 제목이 보이도록 설정
        return self.title

    @classmethod
    def fetch_and_save_data(cls):
        """알라딘 API에서 데이터를 가져와 DB에 저장하는 클래스 메서드"""
        TTB_KEY = 'ttbjuntai03121739001' 
        URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'

        params = {
            'ttbkey': TTB_KEY,
            'QueryType': 'ItemNewAll',   # 요구사항: 전체 신간 리스트
            'MaxResults': 20,            # 요구사항: 10개 이상 수집
            'start': 1,
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101'
        }

        # 외부 API 요청
        response = requests.get(URL, params=params)
        items = response.json().get('item', [])

        for item in items:
            # 1. fixedPrice가 문자열이나 숫자로 올 수 있으므로 Boolean 변환
            is_fixed = True if str(item.get('fixedPrice')).lower() in ['true', '1'] else False
            
            # 2. isbn 필드 max_length=10에 맞게 슬라이싱 (중요: 에러 방지)
            raw_isbn = item.get('isbn', '')[:10]

            # 3. DB에 저장 (이미 있으면 건너뛰고, 없으면 생성)
            cls.objects.get_or_create(
                isbn=raw_isbn,
                defaults={
                    'author': item.get('author'),
                    'title': item.get('title'),
                    'category_name': item.get('categoryName'),
                    'category_id': item.get('categoryId', 0),
                    'price': item.get('priceSales'),
                    'fixed_price': is_fixed,
                    'pub_date': item.get('pubDate'),
                }
            )