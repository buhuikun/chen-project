from django.db import models

# Create your models here.

class BookInfo(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now=True)

class HeroInfo(models.Model):
    name = models.CharField(max_length=50)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
