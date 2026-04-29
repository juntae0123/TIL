from multiprocessing import context

from django.shortcuts import render, get_object_or_404
from .models import Author

def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    context = {
        'author': author,
    }
    return render(request, 'libraries/detail.html', context)
