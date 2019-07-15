from django import forms

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

