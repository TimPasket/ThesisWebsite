from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
from .models import Post
from .forms import newUserForm

class homePage(ListView):
  model = Post
  template_name = 'index.html'
  ordering = ['-id']
  
class postDetailsPage(DetailView):
  model = Post
  template_name = 'postDetails.html'

class addPostPage(CreateView):
  model = Post
  template_name = 'addPost.html'
  fields = '__all__'

class editPostPage(UpdateView):
  model = Post
  template_name = 'editPost.html'
  fields = ['title', 'body']

class deletePostPage(DeleteView):
  model = Post
  template_name = 'deletePost.html'
  success_url = reverse_lazy('home')

def glossaryPage(request):
  return render(request, 'users/glossary.html')

def registerPage(request):
  form = newUserForm()

  if request.method == 'POST':
    form = newUserForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request, 'Account registered for ' + user)
      return redirect('login')

  context = {'form':form}
  return render(request, 'users/register.html', context)

def loginPage(request):
  form = AuthenticationForm(request.POST)
  context = {'form':form}

  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username , password=password)

    if user is not None:
      login(request, user)
      return redirect('home')
    else: 
      messages.info(request, 'Username OR Password is incorrect')
      return render(request, 'users/login.html', context)
      
  return render(request, 'users/login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('login')