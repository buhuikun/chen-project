from zbest.models import *
from comment.models import *
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect, reverse
from .models import *
from django.conf import settings
from django.core.cache import cache
# Create your views here.

def addcomment(request, id):
    if request.method == "POST":
        content = request.POST.get('content')
        ordergood = OrderGoods.objects.get(pk=id)
        ordergood.state = False
        order = ordergood.order
        good = Goods.objects.get(pk=ordergood.good.id)
        comment = Comment()
        comment.content = content
        comment.good = good
        comment.account = cache.get('user')
        ordergood.save()
        comment.save()
        count = order.ordergoods_set.filter(state=1).count()
        if count == 0:
            order.state = '已完成'
            order.save()
    return render(request, 'zbest/commentok.html')





