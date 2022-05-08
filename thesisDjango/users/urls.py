from django.urls import path
from .views import homePage, postDetailsPage, addPostPage
from .import views

urlpatterns = [
    path('', homePage.as_view(), name='home'),
    path('post/<int:pk>', postDetailsPage.as_view(), name='postDetails'),
    path('add-Post', addPostPage.as_view(), name='addPost'),
    path('glossary', views.glossaryPage, name='glossary'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout')
]
