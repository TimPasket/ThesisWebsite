from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *
from .forms import newUserForm

def homePage (request):
  return render(request, 'users/index.html')

def glossaryPage (request):
  return render(request, 'users/glossary.html')

def registerPage(request):
  form = newUserForm()

  if request.method == 'POST':
    form = newUserForm(request.POST)
    if form.is_valid():
      form.save()

  context = {'form':form}
  return render(request, 'users/register.html', context)

def loginPage(request):
  context = {}
  return render(request, 'users/login.html', context)