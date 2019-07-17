from django.db import models
from comment import *
import uuid

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Account(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    portrait = models.ImageField(upload_to='portrait')
    email = models.EmailField(default='123@a.com')

    def __str__(self):
        return self.username


class Goods(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.FloatField()
    seller = models.ForeignKey(Account, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    showimg = models.ImageField(upload_to='showimg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class GoodsImg(models.Model):
    img = models.ImageField(upload_to='goodimg')
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)



class ShoppingCart(models.Model):
    title = models.ForeignKey(Goods, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    number = models.IntegerField()


class Order(models.Model):
    orderid = models.UUIDField(default=uuid.uuid4, null=False,
                           verbose_name=u'app uuid',
                           help_text="app uuid")
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    total = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=10, default='待支付')
    def __str__(self):
        return self.state

class OrderGoods(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    number = models.IntegerField()
