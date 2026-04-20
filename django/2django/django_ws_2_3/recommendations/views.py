# [recommendations/views.py]
import requests
from django.shortcuts import render

def recommend(request):
    TTB_KEY = 'ttbjuntai03121739001'
    URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    
    params = {
        'ttbkey': TTB_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': 50,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(URL, params=params)
    data = response.json()
    items = data.get('item', [])

    # 수집은 4가지(제목, 저자, 출간일, ISBN) 모두 수행
    book_list = []
    for item in items:
        book_list.append({
            'title': item.get('title', '제목 없음'),
            'author': item.get('author', '저자 미상'),
            'pubDate': item.get('pubDate'),
            'isbn': item.get('isbn'),
        })

    context = {
        'books': book_list
    }
    return render(request, 'recommendations/recommend.html', context)