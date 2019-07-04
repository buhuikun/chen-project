from django.db import models

# Create your models here.

class Vote(models.Model):
    title = models.CharField(max_length=100)

class Option(models.Model):
    option = models.CharField(max_length=100)
    num = models.IntegerField()
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
