# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)  # Only need email for signup

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
