from django.urls import path
from .import views

urlpatterns = [
    path('index.html', views.homePage),
    path('glossary.html', views.glossaryPage),
    path('register.html', views.registerPage),
    path('login.html', views.loginPage)
]
