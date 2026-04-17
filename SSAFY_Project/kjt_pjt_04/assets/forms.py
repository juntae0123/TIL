from django import forms

from .models import Post


BAD_WORDS = [
    "욕설",
    "혐오",
    "비방",
    "fuck",
    "shit",
    "kill",
    "death",
    "hate",
    "bitch",
    "asshole",
]


def get_forbidden_tokens(text):
    if not text:
        return []
    lower_text = text.lower()
    return [word for word in BAD_WORDS if word in lower_text]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력하세요'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '작성자 (선택)'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title", "")
        content = cleaned_data.get("content", "")
        forbidden = set(get_forbidden_tokens(title) + get_forbidden_tokens(content))
        if forbidden:
            raise forms.ValidationError(
                "부적절한 내용이 포함되어 있습니다. 수정 후 다시 등록해 주세요."
            )
        return cleaned_data

