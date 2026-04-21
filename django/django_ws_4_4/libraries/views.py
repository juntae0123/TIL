# libraries/views.py
from django.http import HttpResponse
from .models import Book

def index(request):
    # 1. 모델의 클래스 메서드를 호출하여 API 수집 및 DB 저장 실행
    # 이 한 줄로 모든 수집 프로세스가 끝납니다.
    Book.fetch_and_save_data()
    
    # 2. 템플릿 파일이 없어도 에러가 나지 않도록 문자열 응답 반환
    return HttpResponse("알라딘 신간 데이터 수집이 완료되었습니다! 관리자 페이지(/admin)를 확인하세요.")