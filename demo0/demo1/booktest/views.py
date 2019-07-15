import io
import random

from PIL import ImageDraw, Image, ImageFont
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.views.generic import View, TemplateView
from .models import HeroInfo, BookInfo, Ads
from .form import *
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
# MVT 中核心V视图
# 接收请求，处理数据，返回响应
# Create your views here.






# 一个装饰器判断是否登录
def checklogin(fun):
    def check(request, *args):
        # 使用cookies
        # username = request.COOKIES.get('username')
        # 使用session
        username = request.session.get('username')
        if username:
            return fun(request, *args)
        else:
            return redirect(reverse('booktest:login'))
    return check


# 类视图
class IndexView(View):
    def get(self, request):

        ads = Ads.objects.all()
        # 使用cookie
        # username = request.COOKIES.get('username')
        # 使用session
        username = request.session.get('username')
        return render(request, 'booktest/index.html', {'username':username, 'ads': ads})


# 自定义视图函数
def index(request):
    # return HttpResponse('<h1>项目首页面</h1> <a href="/list/">列表页</a>')
    # temp1 = loader.get_template('booktest/index.html')
    # resutl = temp1.render({'username': 'chen'})
    # return HttpResponse(resutl)


    return render(request, 'booktest/index.html', {'username': 'chen'})


@checklogin
def list(request):
    # s="""
    #
    # <a href="/detail/1/">详情1</a>
    # <a href="/detail/2/">详情2</a>
    # <a href="/detail/3/">详情3</a>
    #
    # """
    # return HttpResponse('<h1>项目列表页</h1>%s'%(s, ))
    # temp2 = loader.get_template('booktest/list.html')
    # books = BookInfo.objects.all()
    # resutl = temp2.render({'books':books})
    # return HttpResponse(resutl)
    books = BookInfo.objects.all()
    return render(request, 'booktest/list.html', {'books': books})


@checklogin
def detail(request, id):
    # return HttpResponse('<h1>项目%s详情页</h1> <a href="/">首页</a>'%(id,))
    # temp3 = loader.get_template('booktest/detail.html')
    # book = BookInfo.objects.get(pk=id)
    # # pk表示主键，get表示查找主键为id的
    #
    # resutl = temp3.render({'book':book})
    # return HttpResponse(resutl)
    book = BookInfo.objects.get(pk=id)
    return render(request, 'booktest/detail.html', {'book': book})


@checklogin
def deletehero(request, id):
    hero = HeroInfo.objects.get(pk=id)
    bookid = hero.book.id
    hero.delete()
    # return HttpResponseRedirect('/detail/%s/'%(bookid, ))
    return redirect(reverse('booktest:detail', args=(bookid, )))


@checklogin
def deletebook(request, id):
    book = BookInfo.objects.get(pk=id)
    book.delete()
    return redirect(reverse('booktest:list'))


@checklogin
def addhero(request,id):
    book = BookInfo.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'booktest/addhero.html', {'book':book})
    elif request.method == 'POST':
        name = request.POST.get('username')
        content = request.POST.get('content')
        gender = request.POST.get('gender')
        HeroInfo.objects.addhero(name, gender, content, book)
        # hero = HeroInfo()
        # hero.name = name
        # hero.gender = gender
        # hero.content = content
        # hero.book = book
        # hero.save()
        return redirect(reverse('booktest:detail', args=(book.id, )))


@checklogin
def addbook(request):
    if request.method == "GET":
        return render(request, 'booktest/addbook.html',{})
    elif request.method == 'POST':
        title = request.POST.get('title')
        book = BookInfo()
        book.title = title
        book.save()
        return redirect(reverse('booktest:list'))


@checklogin
def upload(request):
    if request.method == 'GET':
        return render(request, 'booktest/upload.html')
    elif request.method == 'POST':
        # 创建实例
        ads = Ads()
        # 获取HTML页面数据
        ads.desc = request.POST.get('desc')
        ads.img = request.FILES['uploadimg']
        ads.save()

        return redirect(reverse('booktest:index'))




def login(request):
    if request.method == 'GET':
        a = ['2271992921@qq.com']
        # send_mail('aa','12313', settings.EMAIL_HOST_USER,a)


        lgf = LoginForm()
        return render(request, 'booktest/login.html', {'lgf': lgf})
    elif request.method == 'POST':
        # 使用cookie
        # response = redirect(reverse('booktest:index'))
        # response.set_cookie('username', request.POST.get('username'))
        # return response

        # 使用session
        request.session['username'] = request.POST.get('username')
        code = cache.get('rand_str').lower()
        if request.POST.get('verifycode').lower() != code:
            return HttpResponse('验证码错误')
        return redirect(reverse('booktest:index'))


def logout(request):
    # 使用cookie
    # res = redirect(reverse('booktest:login'))
    # res.delete_cookie('username')
    # return res

    request.session.flush()
    return redirect(reverse('booktest:login'))


def verify(request):
    # 定义变量， 用于画面的背景色、 宽、 高
    global xy
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    height = 35
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 300):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABqwertCD1iop23EcmFGasdfHIJK456LMNhjkOPQgR8S7vbn9TUVzWXxYZ0yul'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    cache.set('rand_str', rand_str)
    # 构造字体对象
    font = ImageFont.truetype('BAUHS93.TTF', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端， MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')



