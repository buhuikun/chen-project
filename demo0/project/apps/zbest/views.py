import io
import random

from PIL import ImageFont, ImageDraw, Image
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect, reverse
from .models import *
import hashlib
from django.conf import settings
from django.core.cache import cache
from comment.models import *


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


# Create your views here.
# 注册判断用户名是否存在
def checkuser(request):
    name = request.GET.get('regname')
    user = Account.objects.filter(username=name)

    if user:
        return JsonResponse({'status': 0})
    else:
        return JsonResponse({'status': 1})


# 判断登录
def checklogin(fun):
    def check(request, *args):
        user = cache.get('user')
        if user:
            return fun(request, *args)
        else:
            return redirect(reverse('zbest:login'))

    return check


# 加密密码
def encryption(pwd):
    s = pwd + settings.SECRET_KEY
    return hashlib.sha1(s.encode('utf-8')).hexdigest()


class IndexView(View):
    def get(self, request):
        user = cache.get('user')
        chaungyi = Category.objects.filter(title='创意家居').first().goods_set.order_by('-id')[:3]
        baijian = Category.objects.filter(title='装饰摆件').first().goods_set.order_by('-id')[:3]
        bihua = Category.objects.filter(title='墙式壁挂').first().goods_set.order_by('-id')[:4]
        return render(request, 'zbest/index.html', locals())


class ListView(View):
    def get(self, request, id):
        user = cache.get('user')
        goods = Category.objects.get(pk=id).goods_set.all()
        return render(request, 'zbest/list.html', locals())


class AllView(View):
    def get(self, request):
        user = cache.get('user')
        goods = Goods.objects.all()
        return render(request, 'zbest/list.html', locals())


class PaintView(View):
    def get(self, request):
        user = cache.get('user')
        goods = Category.objects.filter(title='墙式壁挂')[0]
        goods1 = goods.goods_set.order_by('-id')[:6]
        goods2 = goods.goods_set.order_by('-id')[6:12]
        goods3 = goods.goods_set.order_by('-id')[12:16]
        goods4 = goods.goods_set.order_by('-id')[16:19]
        return render(request, 'zbest/paint.html', locals())


class PerfumeView(View):
    def get(self, request):
        user = cache.get('user')
        goods = Category.objects.filter(title='蜡艺香薰')[0]
        goods1 = goods.goods_set.order_by('-id')[:6]
        goods2 = goods.goods_set.order_by('-id')[6:12]
        return render(request, 'zbest/perfume.html', locals())


class IdeaView(View):
    def get(self, request):
        user = cache.get('user')
        goods = Category.objects.filter(title='创意家居')[0]
        goods1 = goods.goods_set.order_by('-id')[:3]
        goods2 = goods.goods_set.order_by('-id')[3:7]
        goods3 = goods.goods_set.order_by('-id')[7:11]
        return render(request, 'zbest/idea.html', locals())


def register(request):
    if request.method == 'GET':
        return render(request, 'zbest/login.html')
    elif request.method == 'POST':
        name = request.POST.get('regname')
        password = request.POST.get('regpass')
        user = Account()
        user.username = name
        user.password = encryption(password)
        user.save()
        return redirect(reverse('zbest:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'zbest/login.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = encryption(request.POST.get('pass'))
        user = Account.objects.filter(username=name, password=password).first()
        if user:
            cache.set('user', user)
            return redirect(reverse('zbest:index'))
        else:
            return render(request, 'zbest/login.html', {'error': '用户名或密码错误！'})


def logout(request):
    cache.delete('user')
    return redirect(reverse('zbest:index'))


@checklogin
def detail(request, id):
    good = Goods.objects.get(pk=id)
    categories = cache.get('categories')
    tuijian = good.category.goods_set.all()[:3]
    num = 1
    comment = Comment.objects.filter(good=good).all()
    return render(request, 'zbest/detail.html', locals())


# class DetailView(View):
#     def get(self, request, id):
#         good = Goods.objects.get(pk=id)
#         categories = cache.get('categories')
#         tuijian = good.category.goods_set.all()[:3]
#         num = 1
#         comment = Comment.objects.filter(good=good).all()
#         return render(request, 'zbest/detail.html', locals())


@checklogin
def center(request):
    user = cache.get('user')
    o2 = user.order_set.filter(state='待收货').count()
    o3 = user.order_set.filter(state='已收货').count()
    o1 = user.order_set.filter(state='未支付').count()
    return render(request, 'zbest/center.html', locals())


@checklogin
def myorder(request):
    orders = Order.objects.all().order_by('-create_time')
    user = cache.get('user')
    pages = getpage(request, orders, per_num=2)
    return render(request, 'zbest/myorder.html', locals())


@checklogin
def myorderzt(request, id):
    state = ''
    if id == '1':
        state = '未支付'
    elif id == '2':
        state = '待收货'
    elif id == '3':
        state = '已收货'
    orders = Order.objects.filter(state=state).order_by('-create_time')
    user = cache.get('user')
    return render(request, 'zbest/myorder.html', locals())


@checklogin
def cart(request):
    user = cache.get('user')
    cart = user.shoppingcart_set.all()
    return render(request, 'zbest/cart.html', locals())


@checklogin
def order(request, id):
    order = Order.objects.get(pk=id)
    ordergoods = order.ordergoods_set.all()

    return render(request, 'zbest/order.html', locals())


@checklogin
def createorder(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        num = request.POST.get('num')
        good = Goods.objects.get(pk=id)
        user = cache.get('user')
        # 订单
        order = Order()
        order.account = user
        order.total = int(num) * good.price
        order.save()
        # 订单商品
        ordergoods = OrderGoods()
        ordergoods.good = good
        ordergoods.number = num
        ordergoods.order = order
        ordergoods.save()
        return JsonResponse({'info': 1, 'orderid': order.id})


# 点击立即购买
@checklogin
def buy(request, id):
    order = Order.objects.get(pk=id)
    order.state = '待收货'
    order.save()
    goods1 = Goods.objects.all().order_by('-create_time')[:5]
    goods2 = Goods.objects.all().order_by('-create_time')[5:10]
    return render(request, 'zbest/ok.html', {'goods1': goods1, 'goods2': goods2})


@checklogin
def addcart(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        num = request.POST.get('num')
        good = Goods.objects.get(pk=id)
        cart = ShoppingCart()
        cart.title = good
        cart.account = cache.get('user')
        cart.number = num
        cart.save()
        return JsonResponse({'info': '添加成功'})


@checklogin
def delcart(request, id):
    ShoppingCart.objects.get(pk=id).delete()
    return redirect(reverse('zbest:cart'))


@checklogin
def createcartorder(request):
    if request.method == 'POST':
        goodlist = request.POST.getlist("goodslist")
        order = Order()
        # 创建订单
        order.account = cache.get('user')
        order.total = 0
        order.save()
        # 遍历购物车中的商品
        for cartid in goodlist:
            cart = ShoppingCart.objects.get(pk=cartid)
            good = cart.title
            num = cart.number
            # 每一个商品价格乘以数量
            goodprice = good.price * int(num)
            # 创建订单的商品
            ordergoods = OrderGoods()
            ordergoods.good = good
            ordergoods.number = num
            ordergoods.order = order
            # 计算订单总价
            order.total += goodprice
            order.save()
            ordergoods.save()
        return redirect(reverse('zbest:order', args=(order.id,)))


@checklogin
def confirm(request, id):
    order = Order.objects.get(pk=id)
    order.state = '已收货'
    order.save()
    return redirect(reverse('zbest:myorder'))


@checklogin
def orderxq(request, id):
    order = Order.objects.get(pk=id)
    user = cache.get('user')
    return render(request, 'zbest/orderxq.html', locals())


@checklogin
def myprod(request):
    ordergoods = Order.objects.filter(state='已收货')
    goods = []
    for orders in ordergoods:
        for order in orders.ordergoods_set.all():
            print(order.good.comment_set.count(), 'adaaaaaaa')
            if order.state:
                goods.append(order)
    user = cache.get('user')
    return render(request, 'zbest/myprod.html', {'user': user, 'goods': goods})


@checklogin
def mygrxx(request):
    user = Account.objects.get(pk=cache.get('user').id)
    return render(request, 'zbest/mygrxx.html', locals())


@checklogin
def changexx(request):
    if request.method == 'POST':
        user = Account.objects.get(pk=cache.get('user').id)
        nickname = request.POST.get('nickname')
        email = request.POST.get('mail')
        gender = request.POST.get('gender')
        user.nickname = nickname
        user.gender = gender
        user.email = email
        user.save()
        cache.delete('user')
        cache.set('user', user)
        return redirect(reverse('zbest:mygrxx'))


@checklogin
def changetx(request):
    if request.method == 'POST':
        user = Account.objects.get(pk=cache.get('user').id)
        tx = request.FILES['tx']
        user.portrait = tx
        user.save()
        cache.delete('user')
        cache.set('user', user)
        return redirect(reverse('zbest:mygrxx'))


# 修改密码
@checklogin
def remima(request):
    if request.method == 'GET':
        if cache.get('info'):
            info = cache.get('info')
        else:
            info = ''
        cache.delete('info')
        user = cache.get('user')
        return render(request, 'zbest/remima.html', {'info': info, 'user': user})
    elif request.method == "POST":
        user = cache.get('user')
        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')
        aeginpass = request.POST.get('aeginpass')
        code = request.POST.get('code')
        if newpass != aeginpass:
            cache.set('info', '两次密码不一致！')
            return redirect(reverse('zbest:remima'))
        if user.password != encryption(oldpass):
            cache.set('info', '原密码不正确！')
            return redirect(reverse('zbest:remima'))
        if code.upper() != cache.get('rand_str').upper():
            cache.set('info', '验证码错误！')
            return redirect(reverse('zbest:remima'))
        user.password = encryption(aeginpass)
        user.save()
        cache.delete('user')
        cache.set('info', '修改成功！')
        return redirect(reverse('zbest:remima'))


@checklogin
def wuliu(request, id):
    return render(request, 'zbest/wuliu.html')


# 验证码
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
    for i in range(0, 200):
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
    font = ImageFont.truetype('calibrib.ttf', 23)
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
