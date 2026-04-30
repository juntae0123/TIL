# 토스증권 커뮤니티 분석기

Django + Selenium + OpenAI API 기반 주식 커뮤니티 댓글 수집·전처리·증강 웹 애플리케이션.

---

## 디렉토리 구조

```
toss_crawler/
├── manage.py
├── requirements.txt
├── toss_project/          # 프로젝트 설정 패키지
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── toss_app/              # 메인 앱
    ├── __init__.py
    ├── models.py          # CrawlResult DB 모델
    ├── forms.py           # SearchForm (입력 검증)
    ├── urls.py            # 앱 URL 라우팅
    ├── views.py           # 요청 처리 + 서비스 오케스트레이션
    ├── services/
    │   ├── __init__.py
    │   ├── crawler.py     # Selenium 토스증권 크롤러
    │   └── llm_processor.py  # 전처리·증강·요약 (OpenAI)
    └── templates/
        ├── index.html     # 입력 폼 페이지
        └── result.html    # 결과 표시 페이지
```

---

## 실행 방법

### 1. 가상환경 생성 및 패키지 설치

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Chrome 설치 확인

Selenium이 Chrome을 제어합니다. 시스템에 Chrome이 설치되어 있어야 합니다.  
ChromeDriver는 `webdriver-manager`가 자동으로 설치합니다.

### 3. DB 마이그레이션

```bash
python manage.py migrate
```

### 4. 서버 실행

```bash
python manage.py runserver
```

브라우저에서 `http://127.0.0.1:8000` 접속.

---

## 기능 흐름

```
[사용자 입력] 회사명 입력 → POST
       ↓
[crawler.py]  토스증권 검색 → 최상단 종목 클릭 → 커뮤니티 탭 → 댓글 20개 수집
       ↓
[llm_processor.py]
  ① 길이 필터 (MIN 5 / MAX 300자)
  ② IQR 이상치 제거
  ③ 정규표현식 정제 (URL·이모지·특수문자 제거)
  ④ OpenAI: 부적절 댓글 필터링
  ⑤ OpenAI: 의미 보존 증강
  ⑥ OpenAI: 전체 동향 요약
       ↓
[DB 저장] CrawlResult 레코드 생성
       ↓
[result.html] 원본·정제·증강·요약 시각화
```

---

## 환경변수 (선택)

`.env` 파일 또는 shell 환경변수로 관리 권장:

```bash
export OPENAI_API_KEY="sk-proj-..."
export DJANGO_SECRET_KEY="your-production-secret-key"
```

`settings.py`와 `llm_processor.py`에서 `os.getenv()`로 읽습니다.

---

## 주요 의존성

| 패키지 | 역할 |
|--------|------|
| Django 4.2 | 웹 프레임워크 |
| selenium 4.x | 브라우저 자동화 |
| webdriver-manager | ChromeDriver 자동 설치 |
| openai 1.x | GPT API 클라이언트 |
