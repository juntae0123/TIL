import requests

def get_aladin_books():
    # 1. API 기본 정보 설정
    # TTB_KEY는 알라딘에서 발급받은 본인의 키를 입력해야 합니다.
    TTB_KEY = 'ttbjuntai03121739001' 
    URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    
    # 2. 요구사항 파라미터 구성
    params = {
        'ttbkey': TTB_KEY,
        'QueryType': 'ItemNewSpecial',  # 주목할 만한 신간 리스트
        'MaxResults': 50,               # 최대 50개 데이터
        'start': 1,
        'SearchTarget': 'Book',         # 조회 대상: 도서
        'output': 'js',                 # 응답 데이터 JSON 형식
        'Version': '20131101'           # 최신 API 버전
    }

    try:
        # 3. 데이터 요청 및 JSON 변환
        response = requests.get(URL, params=params)
        # 응답 데이터는 요구사항에 따라 JSON(딕셔너리)으로 변경
        data = response.json() 
        
        # 4. 결과에서 필요한 값만 추출하여 출력
        items = data.get('item', [])
        
        for item in items:
            # 요구사항: 제목, 저자, 출간일, ISBN만 수집
            title = item.get('title')
            author = item.get('author')
            pub_date = item.get('pubDate')
            isbn = item.get('isbn')
            
            # 최종 결과 출력
            print(f"제목: {title}")
            print(f"저자: {author}")
            print(f"출간일: {pub_date}")
            print(f"ISBN: {isbn}")
            print("-" * 30)

    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    get_aladin_books()