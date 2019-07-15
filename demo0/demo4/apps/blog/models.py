from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


# Create your models here.

class Ads(models.Model):
    desc = models.CharField(max_length=20)
    img = models.ImageField(upload_to='ads')
    index = models.IntegerField(default=0)

    def __str__(self):
        return self.desc


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


# class BlogUser(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     email = models.EmailField(default='123@qq.com')
#
#     def __str__(self):
#         return self.username


class Article(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    # body = models.TextField()
    body = UEditorField(imagePath='articleimg/')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

