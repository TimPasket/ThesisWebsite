from django.urls import path
from .import views

urlpatterns = [
    path('index.html', views.homePage, name="home"),
    path('glossary.html', views.glossaryPage, name="Glossary"),
    path('register.html', views.registerPage, name='register'),
    path('login.html', views.loginPage, name='login'),
    path('/logout', views.logoutUser, name='logout')
]
