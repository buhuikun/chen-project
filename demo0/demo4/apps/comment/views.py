from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Comment
from blog.models import Article


# Create your views here.

class AddComment(View):
    def post(self, request, id):
        name = request.POST.get('name')
        email = request.POST.get('email')
        url = request.POST.get('url')
        content = request.POST.get('content')
        c = Comment()
        c.name = name
        c.url = url
        c.content = content
        c.email = email
        article = Article.objects.get(pk=id)
        c.article = article
        c.save()
        com_num = article.comment_set.count()
        return JsonResponse({'name': name, 'com_num': com_num, 'create_time': c.create_time, 'content': content})
