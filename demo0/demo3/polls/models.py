from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Options(models.Model):
    choice = models.CharField(max_length=50)
    vote = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice




