from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *

def homePage (request):
  return render(request, 'users/index.html')

def glossaryPage (request):
  return render(request, 'users/glossary.html')

def registerPage(request):
  form = UserCreationForm()
  context = {'form'}
  return render(request, 'users/register.html')

def loginPage(request):
  context = {'form'}
  return render(request, 'users/login.html')