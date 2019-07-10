from django import forms
from django.forms.models import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': '文章标题',
            'body':'文章正文',
        }





