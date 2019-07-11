"""
自定义模板表达式
扩展django原有功能
"""

from django.template import library
from blog.models import Article, Category, Tag

register = library.Library()

# 最新三篇文章
@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.order_by('-create_time')[:num]

# 分类
@register.simple_tag
def getcategory():
    return Category.objects.all()

@register.filter
def lower(val, sql):
    return sql.join(val)

# 归档
@register.simple_tag
def gettimes():
    times = Article.objects.dates('create_time', 'month', 'DESC')
    return times


# 标签云
@register.simple_tag
def gettags():
    return Tag.objects.all()