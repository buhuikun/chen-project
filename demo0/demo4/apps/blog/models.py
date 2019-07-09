from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ads(models.Model):
    desc = models.CharField(max_length=20)
    img = models.ImageField(upload_to='ads')
    index = models.IntegerField(default=0)


class Category(models.Model):
    title = models.CharField(max_length=20)

class Tag(models.Model):
    title = models.CharField(max_length=30)


class Article(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
