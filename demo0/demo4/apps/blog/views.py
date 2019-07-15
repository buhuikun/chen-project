from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.views import View

from blog.forms import ArticleForm, CommentForm, LoginForm, RegistForm
from .models import *
from django.core.paginator import Paginator
from django.core.cache import cache


# Create your views here.

# 获取分页方法
def getpage(request, object_list, per_num=1):
    pagenum = request.GET.get('page')
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, per_num).get_page(pagenum)
    # if int(pagenum) >= 4:
    #     a = page.paginator.page_range[int(pagenum) - 3:int(pagenum) + 2]
    # else:
    #     a = range(1, 6)
    return page


def checklogin(fun):
    def check(request, *args):
        username = cache.get('username')
        if username:
            return fun(request, *args)
        else:
            return redirect(reverse('blog:login'))
    return check


# 主页面
class IndexView(View):
    def get(self, request):
        ads = Ads.objects.all()
        article = Article.objects.all()

        # 获取get参数当前页码，a代表显示的几个页码
        page = getpage(request, article, 2)
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
        page= getpage(request, articles, 2)
        return render(request, 'blog/list.html', {'page': page,})


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
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))
        return HttpResponse('添加失败')


# 归档
class ArchivesView(View):
    def get(self, request, year, month):
        article = Article.objects.filter(create_time__year=year, create_time__month=month)
        page = getpage(request, article, 2)
        return render(request, 'blog/index.html', locals())


# 分类
class CategoryView(View):
    def get(self, request, id):
        category = Category.objects.get(pk=id)
        article = category.article_set.all()
        page= getpage(request, article, 2)
        return render(request, 'blog/index.html', locals())


# 标签
class TagsView(View):
    def get(self, request, id):
        tags = Tag.objects.get(pk=id)
        article = tags.article_set.all()
        page = getpage(request, article, 2)
        return render(request, 'blog/index.html', locals())


def login(request):
    if request.method == 'GET':
        lgf = LoginForm()
        return render(request, 'blog/login.html', {'lgf': lgf})
    elif request.method == 'POST':
        lgf = LoginForm(request.POST)
        # 判断账户密码是否有效
        if lgf.is_valid():
            # username = lgf.cleaned_data['username']
            # password = lgf.cleaned_data['password']

            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                cache.set('username', username)
                return redirect(reverse('blog:index'))
            else:
                return redirect(reverse('blog:login'))
        return redirect(reverse('blog:login', args=({'error':'账户或密码错误'})))


def register(request):
    if request.method == 'POST':
        rgf = RegistForm(request.POST)
        if rgf.is_valid():
            user = rgf.save(commit=False)
            user.set_password(rgf.cleaned_data['password'])
            user.is_active = False
            user.save()

        return render(request, 'blog/login.html')
