from django.db import models

# Create your models here.

class Questions(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now=True)


class Options(models.Model):
    name = models.CharField(max_length=50)
    vote = models.IntegerField(default=0)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

