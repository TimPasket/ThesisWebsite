from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .models import *
from .forms import newUserForm, loginForm

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
      return redirect('loginPage')

  context = {'form':form}
  return render(request, 'users/register.html', context)

def loginPage(request):
  if request.method == "POST":
    username = request.POST.get('loginUsername')
    password = request.POST.get('loginPassword')
    user = authenticate(request, username=username , password=password)

    if user is not None:
      login(request, user)
      return redirect('Home')

  context = {}
  return render(request, 'users/login.html', context)