from django.shortcuts import render,redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth import login as lgi, logout as lgo, authenticate


# Create your views here.

def checklogin(fun):
    def check(request, *args):
        # 使用cookie
        # username = request.COOKIES.get('username')

        # 使用session
        # username = request.session.get('username')
        # if username:
        #     return fun(request, *args)
        # else:
        #     return redirect(reverse('vote:login'))

        # 使用django自带授权
        if request.user and request.user.is_authenticated:
            return fun(request, *args)
        else:
            return redirect(reverse('vote:login'))

    return check


@checklogin
def vindex(request):
    vote = Vote.objects.all()
    # 使用cookie
    # username = request.COOKIES.get('username')
    # 使用session
    # username = request.session.get('username')

    # 使用django自带授权
    username = request.user
    return render(request, 'vote/index.html', {'vote': vote, 'username':username})


@checklogin
def vdetail(request, id):
    vote = Vote.objects.get(pk=id)
    if request.method == 'GET':

        return render(request, 'vote/detail.html', {'vote':vote})
    elif request.method == 'POST':
        optionid = request.POST.get('optionid')
        option = Option.objects.get(pk=optionid)
        option.num+=1
        option.save()
        return redirect(reverse('vote:result', args=(vote.id,)))

@checklogin
# 投票结果
def result(request, id):
    vote = Vote.objects.get(pk=id)
    # locals()返回当前函数内部所有局部变量
    # a = 1
    # print(locals())
    return render(request, 'vote/result.html', locals())


def login(request):
    if request.method == 'GET':
        return render(request, 'vote/login.html')
    elif request.method == 'POST':
        # 使用cookies
        # res = redirect(reverse('vote:vindex'))
        # res.set_cookie('username', request.POST.get('username'))
        # return res

        # 使用session
        # request.session['username'] = request.POST.get('username')
        # return redirect(reverse('vote:vindex'))

        # 使用django自带授权
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            lgi(request, user)
            return redirect(reverse('vote:vindex'))
        else:
            return render(request, 'vote/login.html', {'errors': '登录失败'})

def logout(request):

    # 使用cookies
    # res = redirect(reverse('vote:login'))
    # res.delete_cookie('username')
    # return res
    # 使用session
    # request.session.flush()
    # return redirect(reverse('vote:vindex'))

    # 使用django自带授权
    lgo(request)
    return redirect(reverse('vote:login'))


# 使用django自带授权
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = VoteUser.objects.create_user(username=username, password=password)
        except:
            user = None
        if user:
            return redirect(reverse('vote:vindex'))
        else:
            return render(request, 'vote/login.html', {'errors': '注册失败'})
