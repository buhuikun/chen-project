from django import forms
from django.forms.models import ModelForm
from .models import Article
from comment.models import Comment
from django.contrib.auth.models import User


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

class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={'id':'username',
                   'class':'form-control',
                   'placeholder': '输入用户名',
                   }))

    password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id':'password',
            'placeholder':'输入密码！',
        }))

class RegistForm(forms.ModelForm):
    repeatpassword = forms.CharField(label="重复密码",required=True,widget=forms.PasswordInput(attrs={"class":"form-control","id":"registpassword2", "placeholder":"输入确认密码"}))
    class Meta:
        model = User
        fields = ["username","password",'email']
        widgets = {
            "username":forms.TextInput(attrs={"id":"registusername","placeholder":"输入用户名","class":"form-control" }),
            "password":forms.PasswordInput(attrs={"class":"form-control","id":"registpassword", "placeholder":"输入密码"}),
       }
        help_texts = {
            "username":"",
        }
        labels = {
            "telepone":"手机号"
        }

