from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.views import View

from blog.forms import ArticleForm, CommentForm
from .models import *
from django.core.paginator import Paginator


# Create your views here.

# 获取分页方法
def getpage(request, object_list, per_num=1):
    pagenum = request.GET.get('page')
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, per_num).get_page(pagenum)
    if int(pagenum) >= 4:
        a = page.paginator.page_range[int(pagenum) - 3:int(pagenum) + 2]
    else:
        a = range(1, 6)
    return page, a


# 主页面
class IndexView(View):
    def get(self, request):
        ads = Ads.objects.all()
        article = Article.objects.all()

        # 获取get参数当前页码，a代表显示的几个页码
        page, a = getpage(request, article, 1)
        return render(request, 'blog/index.html', locals())


# 文章详情
class SingleView(View):

    def get(self, request, id):
        # article = Article.objects.get(pk=id)
        # 有异常处理
        article = get_object_or_404(Article, pk=id)
        article.views += 1
        article.save()
        # 生成comment表单
        cf = CommentForm()
        return render(request, 'blog/single.html', {'article': article, 'cf': cf})

    def post(self, request, id):
        article = Article.objects.get(pk=id)
        # 获取comment表单
        cf = CommentForm(request.POST)
        comment = cf.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(reverse('blog:single', args=(article.id,)))


# 文章列表
class ListView(View):
    def get(self, request):
        articles = Article.objects.all()
        page, a = getpage(request, articles, 2)
        return render(request, 'blog/list.html', {'page': page, 'a': a})


# 联系页面
def contact(request):
    return render(request, 'blog/contact.html')


# 添加文章
class AddArticle(View):
    def get(self, request):
        af = ArticleForm()
        return render(request, 'blog/addarticle.html', locals())

    def post(self, request):
        af = ArticleForm(request.POST)
        if af.is_valid():
            article = af.save(commit=False)
            article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))
        return HttpResponse('添加失败')


# 归档
class ArchivesView(View):
    def get(self, request, year, month):
        article = Article.objects.filter(create_time__year=year, create_time__month=month)
        page, a = getpage(request, article, 1)
        return render(request, 'blog/index.html', locals())


class CategoryView(View):
    def get(self, request, id):
        category = Category.objects.get(pk=id)
        article = category.article_set.all()
        page, a = getpage(request, article, 1)
        return render(request, 'blog/index.html', locals())


class TagsView(View):
    def get(self, request, id):
        tags = Tag.objects.get(pk=id)
        article = tags.article_set.all()
        page, a = getpage(request, article, 1)
        return render(request, 'blog/index.html', locals())
