from django.db import models
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#login
class LoginPage(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'

#logout
class RegisterPage(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

#publishblog
class PublishBlog(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','image','intro','description']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']