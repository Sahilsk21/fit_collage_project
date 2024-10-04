from django import forms

from .models import UserInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'address', 'mobile_number','password'] 




class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)