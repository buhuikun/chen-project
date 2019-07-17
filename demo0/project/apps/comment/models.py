from django.db import models
from zbest.models import Account, Goods


# Create your models here.
class Comment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)

    def __str__(self):
        return self.good
