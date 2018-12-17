from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import MyUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username','email','password1','password2','first_name']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='İstifadəçi adı')
    password = forms.CharField(max_length=128, label='Parol', widget=forms.PasswordInput())