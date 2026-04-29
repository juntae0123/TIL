from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookForm
from .models import Author, Book

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    book_form = BookForm()
    context = {
        'author': author,
        'book_form': book_form,
        'books': books,
    }
    return render(request, 'libraries/detail.html', context)

def books_create(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author # URL에서 받은 저자 정보 수동 주입
            book.save()
    return redirect('libraries:detail', author.pk)