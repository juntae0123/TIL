# bestseller/views.py
import requests
from django.shortcuts import render

def bestseller(request):
    TTB_KEY = 'ttbjuntai03121739001'
    URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    
    params = {
        'ttbkey': TTB_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': 50,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(URL, params=params)
    data = response.json()
    items = data.get('item', [])

    raw_books = []
    for item in items:
        raw_books.append({
            'title': item.get('title', '제목 없음'),
            'author': item.get('author', '저자 미상'),
            'salesPoint': item.get('salesPoint', 0),    # 정렬 기준
            'bestRank': item.get('bestDuration', ''),   # 추가 정보
        })

    # 요구사항: 판매 지수 기준 내림차순 정렬
    sorted_books = sorted(raw_books, key=lambda x: x['salesPoint'], reverse=True)

    context = {
        'books': sorted_books
    }
    # 템플릿 경로가 bestseller/templates/bestseller.html 이라면 아래처럼 작성
    return render(request, 'bestseller.html', context)