from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *

def registerPage(request):
  form = UserCreationForm()
  context = {'form'}
  return render(request, 'Frontend/register.html', context)
def loginPage(request):
  context = {'form'}
  return render(request, 'Frontend/login.html', context)