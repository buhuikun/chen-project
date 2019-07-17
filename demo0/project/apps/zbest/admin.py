from django.contrib import admin
from .models import *

# Register your models here.
# django后台管理

admin.site.register(Category)
admin.site.register(Account)

admin.site.register(Goods)
admin.site.register(GoodsImg)

