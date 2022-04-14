from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory


# Create your views here.
from .models import *
from .forms import OrderForm
from .filters import OrderFilter

def registerPage(request):
  form = UserCreationForm()
  context = {'form'}
  return render(request, 'Frontend/register.html', context)
def loginPage(request):
  context = {}
  return render(request, 'Frontend/login.html', context)