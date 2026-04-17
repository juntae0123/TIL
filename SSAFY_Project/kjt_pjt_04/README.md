# 금융 자산 커뮤니티 Django 프로젝트

이 프로젝트는 Django 기반으로 구현된 금융 자산 토론 게시판입니다. `assets.json`에 정의된 금융 자산 정보를 기반으로 자산별 게시판을 제공하며, 게시글 생성/수정/삭제와 부적절한 콘텐츠 필터링 기능이 포함되어 있습니다.

## 프로젝트 구조

```
manage.py
requirements.txt
README.md
.env.example
assets/
  ├─ admin.py
  ├─ apps.py
  ├─ forms.py
  ├─ models.py
  ├─ urls.py
  ├─ views.py
  ├─ tests.py
  ├─ templates/assets/
  │   ├─ asset_list.html
  │   ├─ asset_detail.html
  │   ├─ post_form.html
  │   └─ post_detail.html
  └─ migrations/
mypjt/
  ├─ settings.py
  ├─ urls.py
  ├─ wsgi.py
  └─ asgi.py
data/
  └─ assets.json
```

## 핵심 기능

### 1. 자산 목록 화면
- `assets.json`에서 금융 자산 데이터를 읽어옵니다.
- 자산 이름, 카테고리, 설명, 위험 수준, 해당 자산에 속한 게시글 수를 함께 보여줍니다.
- 각 자산 항목을 클릭하면 자산별 게시판 상세 페이지로 이동합니다.
- URL 경로: `/assets/`

### 2. 자산별 게시판 화면
- 선택한 자산의 정보(이름, 코드, 카테고리, 위험 수준, 설명)를 카드로 표시합니다.
- 해당 자산에 달린 게시글 목록을 최신순으로 출력합니다.
- 각 게시글 항목에는 제목, 작성자, 작성일 요약 정보를 표시합니다.
- URL 경로: `/assets/<asset_id>/`

### 3. 게시글 상세 보기
- 게시글 제목, 작성자, 생성일, 수정일, 내용 등을 전체 화면으로 출력합니다.
- 수정 버튼과 삭제 버튼을 제공합니다.
- 삭제 시 현재 자산 게시판 목록으로 이동합니다.
- URL 경로: `/assets/<asset_id>/posts/<post_pk>/`

### 4. 게시글 작성 및 수정
- `post_form.html`을 공통으로 사용합니다.
- 작성/수정 화면에서 제목, 내용, 작성자를 입력할 수 있습니다.
- 제목과 내용에 부적절한 단어가 포함된 경우 입력을 차단하고 오류 메시지를 표시합니다.
- URL 경로:
  - 게시글 생성: `/assets/<asset_id>/posts/create/`
  - 게시글 수정: `/assets/<asset_id>/posts/<post_pk>/update/`

### 5. 게시글 삭제
- 게시글 상세 화면에서 삭제 버튼을 눌러 게시글을 삭제합니다.
- 삭제 완료 후 해당 자산 게시판으로 리디렉션합니다.
- URL 경로: `/assets/<asset_id>/posts/<post_pk>/delete/`

## 주요 파일 설명

### `assets/models.py`
- `Post` 모델 정의
  - `asset_id`: `CharField(max_length=50)`
  - `title`: `CharField(max_length=200)`
  - `content`: `TextField`
  - `author`: `CharField(max_length=100, default='익명')`
  - `created_at`: `DateTimeField(auto_now_add=True)`
  - `updated_at`: `DateTimeField(auto_now=True)`

### `assets/views.py`
- `asset_list`: JSON 자산 목록과 게시글 수 표시
- `asset_detail`: 자산별 정보와 게시글 목록 렌더링
- `post_detail`: 게시글 상세 보기
- `post_create`: 게시글 생성 기능
- `post_update`: 게시글 수정 기능
- `post_delete`: 게시글 삭제 기능
- `get_asset_info`: `assets.json`에서 자산 데이터를 조회하는 헬퍼 함수

### `assets/forms.py`
- `PostForm`: `Post` 모델 기반 폼
- `clean()`: 제목/내용에 부적절한 단어가 포함된 경우 validation error 발생

### `assets/urls.py`
- `app_name = 'assets'`
- URL 패턴
  - `path('', views.asset_list, name='asset_list')`
  - `path('<str:asset_id>/', views.asset_detail, name='asset_detail')`
  - `path('<str:asset_id>/posts/create/', views.post_create, name='post_create')`
  - `path('<str:asset_id>/posts/<int:post_pk>/', views.post_detail, name='post_detail')`
  - `path('<str:asset_id>/posts/<int:post_pk>/update/', views.post_update, name='post_update')`
  - `path('<str:asset_id>/posts/<int:post_pk>/delete/', views.post_delete, name='post_delete')`

### `mypjt/urls.py`
- `path('admin/', admin.site.urls)`
- `path('assets/', include('assets.urls'))`

### `mypjt/settings.py`
- `.env` 파일을 로드하도록 `python-dotenv` 설정
- `OPENAI_API_KEY`, `UPSTAGE_API_KEY` 환경변수 읽기

## 화면 설명

### 자산 목록 화면
- 금융 자산 목록을 카드 형태로 나열합니다.
- 각 카드에는 자산명, 카테고리, 설명, 위험 수준, 게시글 수가 표시됩니다.
- 카드 클릭 시 자산별 게시판으로 이동합니다.

### 자산 게시판 화면
- 선택한 자산의 상세 정보를 상단에 표시합니다.
- 해당 자산 게시글 목록을 최신순으로 보여줍니다.
- 글쓰기 버튼으로 새로운 게시글 작성 화면으로 이동합니다.

### 게시글 상세 화면
- 게시글 제목과 작성자, 시간 정보를 페이지 상단에 표시합니다.
- 본문 내용을 전체 형태로 출력합니다.
- 목록, 수정, 삭제 버튼을 제공합니다.

### 게시글 작성/수정 화면
- 제목, 내용, 작성자 입력폼을 표시합니다.
- 부적절한 콘텐츠가 포함되면 오류 메시지가 표시됩니다.
- 작성/수정 후 저장하면 게시글 상세 화면으로 이동합니다.

## 실행 방법

1. 가상환경을 활성화합니다.
2. 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```
3. 데이터베이스 마이그레이션:
   ```bash
   python manage.py migrate
   ```
4. 서버 실행:
   ```bash
   python manage.py runserver
   ```
5. 브라우저에서 접속:
   - `http://127.0.0.1:8000/assets/`
   - 자산 상세 예: `http://127.0.0.1:8000/assets/stock-kospi/`

## 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음 값을 작성합니다:

```text
OPENAI_API_KEY=your_openai_api_key_here
UPSTAGE_API_KEY=your_upstage_api_key_here
```

필요 시 `.env.example` 파일을 참고하세요.

## 테스트

아래 명령어로 `assets` 앱 테스트를 실행할 수 있습니다.

```bash
python manage.py test assets
```

## 의도와 설계

이 프로젝트는 금융 자산별 토론 게시판을 구현하는 데 목적을 두고 있습니다. 핵심 설계 철학은 다음과 같습니다.

- `assets.json`으로 자산 정보를 정의하여, 실제 자산 목록을 코드 변경 없이 확장할 수 있도록 함.
- `Post` 모델은 자산 게시글 저장 전용으로 설계되어, `asset_id`로 자산별 게시판을 구현.
- 게시글 작성과 수정 시 부적절한 내용을 검사하여 게시판 품질을 유지.
- 자산별 게시판 구조, 글 상세 페이지, 수정/삭제 기능을 학교 과제 요구사항(F402/F403/F405/F407/F411/F412)에 맞게 반영.

## 추가 참고

- 자산 목록 화면에서 현재 자산이 없는 경우에는 `assets.json`에 정의된 자산 정보는 나오지만, 게시글 수는 0으로 표시됩니다.
- 실제 자산별 게시판을 동작시키려면 `POST` 모델에 게시글을 먼저 등록해야 합니다.
- `OPENAI_API_KEY`와 `UPSTAGE_API_KEY`는 선택 사항이며, 현재는 간단한 금지어 필터링을 로컬에서 처리하도록 구현되어 있습니다.
