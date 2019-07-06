from django.db import models

# Create your models here.

class BookInfo(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    info = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

