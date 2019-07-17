from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect, reverse
from .models import *
import hashlib
from django.conf import settings
from django.core.cache import cache

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
        categories = Category.objects.all()
        cache.set('categories', categories)
        return render(request, 'zbest/index.html', locals())


class ListView(View):
    def get(self, request, id):
        categories = cache.get('categories')
        goods = Category.objects.get(pk=id).goods_set.all()
        return render(request, 'zbest/list.html', locals())


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


class DetailView(View):
    def get(self, request, id):
        good = Goods.objects.get(pk=id)
        categories = cache.get('categories')
        tuijian = good.category.goods_set.all()[:3]
        num = 1
        return render(request, 'zbest/detail.html', locals())


@checklogin
def center(request, id):
    user = cache.get('user')
    return render(request, 'zbest/center.html', locals())


@checklogin
def myorder(request):
    orders = Order.objects.all()
    user = cache.get('user')
    pages = getpage(request, orders, per_num=2)
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
    return render(request, 'zbest/ok.html')


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
            goodprice = good.price*int(num)
            # 创建订单的商品
            ordergoods = OrderGoods()
            ordergoods.good = good
            ordergoods.number = num
            ordergoods.order = order
            # 计算订单总价
            order.total += goodprice
            order.save()
            ordergoods.save()
        return redirect(reverse('zbest:order', args=(order.id, )))


def confirm(request, id):
    order = Order.objects.get(pk=id)
    order.state = '已收货'
    order.save()
    return redirect(reverse('zbest:myorder'))

def orderxq(request, id):
    order = Order.objects.get(pk=id)
    user = cache.get('user')
    return render(request, 'zbest/orderxq.html', locals())


def myprod(request):
    ordergoods = Order.objects.filter(state='已收货')
    goods = []
    for orders in ordergoods:
        for order in orders.ordergoods_set.all():
            goods.append(order.good)
    user = cache.get('user')
    return render(request, 'zbest/myprod.html', {'user':user, 'goods': goods})



