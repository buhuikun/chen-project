from django.db import models
from blog.models import Article

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField(blank=True,null=True,default='http://www.baidu.com')
    email = models.EmailField(blank=True, null=True)
    content = models.TextField()
    # auth = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


    def __str__(self):
        return self.article