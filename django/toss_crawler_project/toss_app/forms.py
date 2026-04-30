# =============================================================================
# toss_app/forms.py
# 역할: 사용자 입력 유효성 검사 폼 정의 (F101)
# 원리: Django Form 클래스가 HTML 렌더링과 서버 측 검증을 동시에 처리한다.
#       빈 값 제출 방지는 required=True(기본값)로 보장하며,
#       추가로 공백만 입력된 경우도 clean_company_name에서 차단한다.
# =============================================================================

from django import forms


class SearchForm(forms.Form):
    company_name = forms.CharField(
        label="회사명 / 종목명",
        max_length=50,
        min_length=1,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "예: 삼성전자, 카카오, NAVER",
                "autofocus": True,
            }
        ),
        error_messages={
            "required": "회사명을 입력해 주세요.",
            "min_length": "한 글자 이상 입력해 주세요.",
        },
    )

    def clean_company_name(self):
        value = self.cleaned_data.get("company_name", "").strip()
        if not value:
            raise forms.ValidationError("공백만으로는 검색할 수 없습니다.")
        return value
