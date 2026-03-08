# requests 패키지 사용 예제
# requests 패키지 설치해야 정상 동작

import requests

# 공휴일 정보 API
url = "https://date.nager.at/api/v3/publicholidays/2026/KR"
response = requests.get(url).json() #URL 주소에 요청을보내서 응답 데이터를 받아 딕셔너리로 변경하는 코드
print(response)
