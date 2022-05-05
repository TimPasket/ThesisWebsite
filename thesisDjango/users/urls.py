from django.urls import path
from .views import homePage
from .import views

urlpatterns = [
    path('', homePage.as_view(), name='home'),
    path('glossary', views.glossaryPage, name='glossary'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout')
]
