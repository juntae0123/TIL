# libraries/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('author',) # 저자 선택칸 숨기기