from django.contrib import admin
from .models import *

# Register your models here.
# django后台管理

class HeroInfoInlines(admin.StackedInline):
    model = HeroInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    # 需要显示的内容
    list_display = ('title', 'pub_date')
    # 过滤
    list_filter = ('title', )
    # 分页
    list_per_page = 1
    # 搜索（关键字）
    search_fields = ('title', 'name')
    # 添加book同时可以添加hero
    inlines = [HeroInfoInlines]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)


