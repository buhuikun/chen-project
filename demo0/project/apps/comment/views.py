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
    return HttpResponse('添加成功')





