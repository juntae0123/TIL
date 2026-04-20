import requests
from django.shortcuts import render

def index(request):
    TTB_KEY = 'ttbjuntai03121739001' 
    URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'

    params = {
        'ttbkey': TTB_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': 50,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(URL, params=params)
    data = response.json()
    items = data.get('item', [])

    book_list = []

    for item in items:
        book_list.append({
            'title': item.get('title'),
            'author': item.get('author'),
            'pub_date': item.get('pubDate'),
            'isbn': item.get('isbn'),
        })

    context = {
        'books' : book_list
    }
    return render(request, 'libraries/index.html', context)