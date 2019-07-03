from django.shortcuts import render
from .models import HeroInfo, BookInfo

def index(request):
    return render(request, 'booktest/index.html', {'username': 'chen'})


def list(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/list.html', {'books': books})


def detail(request, id):
    book = BookInfo.objects.get(pk=id)
    return render(request, 'booktest/detail.html', {'book': book})