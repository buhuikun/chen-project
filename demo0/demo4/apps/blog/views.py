from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from django.views import View

from blog.forms import ArticleForm
from .models import *
from django.core.paginator import Paginator


# Create your views here.

class IndexView(View):
    def get(self, request):
        ads = Ads.objects.all()
        article = Article.objects.all()

        # 获取get参数当前页码
        pagenum = request.GET.get('page')
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(article, 1).get_page(pagenum)

        return render(request, 'blog/index.html', locals())


class SingleView(View):

    def get(self, request, id):
        article = Article.objects.get(pk=id)
        return render(request, 'blog/single.html', {'article': article})

    def post(self, request, id):
        article = Article.objects.get(pk=id)
        return render(request, 'blog/single.html', {'article': article})


class ListView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'blog/list.html', {'articles': articles})

    def post(self, request):
        return render(request, 'blog/list.html')


class AddArticle(View):
    def get(self, request):
        af = ArticleForm()
        return render(request, 'blog/addarticle.html', locals())

    def post(self, request):
        af = ArticleForm()
        if af.is_valid():
            article = af.save(commit=False)
            article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))
        return HttpResponse('添加失败')
