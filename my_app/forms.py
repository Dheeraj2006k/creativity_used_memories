from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms import ModelForm
from .models import post



class UserRegistrationForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['username','email','password1','password2']



class UserLoginForm(AuthenticationForm):
    class Meta :
        model = User
        fields = ['username','password']

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'subtitle', 'content', 'image']