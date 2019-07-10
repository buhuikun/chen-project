"""
自定义模板表达式
扩展django原有功能
"""

from django.template import library
from blog.models import Article, Category

register = library.Library()


@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.order_by('-create_time')[:num]

@register.simple_tag
def getcategory():
    return Category.objects.all()
