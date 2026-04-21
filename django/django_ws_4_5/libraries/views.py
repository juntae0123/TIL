# [libraries/views.py]
from django.shortcuts import render
from .models import Book

def index(request):
    # 클래스 메서드 호출하여 데이터 동기화
    Book.fetch_and_save_data()
    
    # 저장된 전체 데이터 조회
    books = Book.objects.all()
    return render(request, 'libraries/index.html', {'books': books})