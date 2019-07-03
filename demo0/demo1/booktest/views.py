from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import HeroInfo, BookInfo
# MVT 中核心V视图
# 接收请求，处理数据，返回响应
# Create your views here.

# 自定义视图函数
def index(request):
    # return HttpResponse('<h1>项目首页面</h1> <a href="/list/">列表页</a>')
    # temp1 = loader.get_template('booktest/index.html')
    # resutl = temp1.render({'username': 'chen'})
    # return HttpResponse(resutl)
    return render(request, 'booktest/index.html', {'username': 'chen'})

def list(request):
    s="""
    
    <a href="/detail/1/">详情1</a>
    <a href="/detail/2/">详情2</a>
    <a href="/detail/3/">详情3</a>
     
    """
    # return HttpResponse('<h1>项目列表页</h1>%s'%(s, ))
    # temp2 = loader.get_template('booktest/list.html')
    # books = BookInfo.objects.all()
    # resutl = temp2.render({'books':books})
    # return HttpResponse(resutl)
    books = BookInfo.objects.all()
    return render(request, 'booktest/list.html', {'books': books})

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