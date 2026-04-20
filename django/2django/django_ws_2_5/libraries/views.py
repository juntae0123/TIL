# [libraries/views.py] 도서 데이터 처리 로직
import requests
from django.shortcuts import render

# API 공통 설정
TTB_KEY = '본인의_TTB_KEY_입력'
URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'

def index(request):
    """메인 페이지: 서비스 소개 문구 출력"""
    return render(request, 'libraries/index.html')

def recommend(request):
    """추천 페이지: 주목할 만한 신간 리스트"""
    params = {
        'ttbkey': TTB_KEY, 'QueryType': 'ItemNewSpecial',
        'MaxResults': 50, 'SearchTarget': 'Book', 'output': 'js', 'Version': '20131101'
    }
    response = requests.get(URL, params=params).json()
    items = response.get('item', [])
    
    books = []
    for item in items:
        books.append({
            'title': item.get('title'),
            'author': item.get('author'),
        })
    return render(request, 'libraries/recommend.html', {'books': books})

def bestseller(request):
    """베스트셀러 페이지: 판매지수 기준 정렬 및 1~3위 강조용 데이터 전달"""
    params = {
        'ttbkey': TTB_KEY, 'QueryType': 'Bestseller',
        'MaxResults': 50, 'SearchTarget': 'Book', 'output': 'js', 'Version': '20131101'
    }
    response = requests.get(URL, params=params).json()
    items = response.get('item', [])
    
    books = []
    for item in items:
        books.append({
            'title': item.get('title'),
            'author': item.get('author'),
            'salesPoint': item.get('salesPoint', 0),
            'bestRank': item.get('bestDuration', ''),
        })
    
    # 판매 지수 기준 내림차순 정렬
    sorted_books = sorted(books, key=lambda x: x['salesPoint'], reverse=True)
    return render(request, 'libraries/bestseller.html', {'books': sorted_books})