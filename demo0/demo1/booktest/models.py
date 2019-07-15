from django.db import models
from django.contrib.auth.models import User
# MVT中的M数据模型
# Create your models here.


class BookInfo(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HeroInfoManage(models.Manager):
    def addhero(self, name, gender, content, book):
        hero = HeroInfo()
        hero.name = name
        hero.gender = gender
        hero.content = content
        hero.book = book
        hero.save()

class HeroInfo(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=(('m','男'), ('w', '女')))
    # gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    objects = HeroInfoManage()
    def __str__(self):
        return self.name


class Ads(models.Model):
    desc = models.CharField(max_length=20)
    img = models.ImageField(upload_to='img')

    def __str__(self):
        return self.desc



