from django.urls import path
from .import views

urlpatterns = [
    path('index.html', views.homePage, name="Home"),
    path('glossary.html', views.glossaryPage, name="Glossary"),
    path('register.html', views.registerPage),
    path('login.html', views.loginPage, name='loginPage')
]
