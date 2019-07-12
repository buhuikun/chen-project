from django import forms
from django.forms.models import ModelForm
from .models import Article
from comment.models import Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': '文章标题',
            'body':'文章正文',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content', 'url', 'email']



