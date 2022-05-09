from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Comment

class newUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username' , 'email', 'password1', 'password2']

class commentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'body')

    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
    }