from django.shortcuts import render, redirect,reverse


from .models import *
# Create your views here.

def index(request):
    return render(request, 'booktest/index.html', {})

def detail(request, id):
    book = BookInfo.objects.get(pk=id)
    return render(request, 'booktest/detail.html', {'book': book})

def list(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/list.html', {'books':books})

def addhero(request, id):
    book = BookInfo.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'booktest/addhero.html', {'book': book})
    elif request.method == 'POST':
        hero = HeroInfo()
        hero.name = request.POST.get('name')
        hero.info = request.POST.get('info')
        hero.gender = request.POST.get('gender')
        hero.book = book
        hero.save()
        return redirect(reverse('booktest:detail', args=(book.id, )))


def delhero(request, id):
    hero = HeroInfo.objects.get(pk=id)
    book = hero.book
    hero.delete()
    return redirect(reverse('booktest:detail', args=(book.id,)))

def addbook(request):
    if request.method == 'GET':
        return render(request, 'booktest/addbook.html', {})
    elif request.method == 'POST':
        book = BookInfo()
        book.title = request.POST.get('title')
        book.save()
        return redirect(reverse('booktest:list'))

def delbook(request, id):
    book = BookInfo.objects.get(pk=id)
    book.delete()
    return redirect(reverse('booktest:list'))
