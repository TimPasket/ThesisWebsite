from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import homePage, postDetailsPage, addPostPage, editPostPage, deletePostPage
from .import views

urlpatterns = [
    path('', homePage.as_view(), name='home'),
    path('post/<int:pk>', postDetailsPage.as_view(), name='postDetails'),
    path('add-Post', login_required(addPostPage.as_view(),login_url='login'), name='addPost'),
    path('post/edit/<int:pk>', login_required(editPostPage.as_view(),login_url='login'), name='editPost'),
    path('post/<int:pk>/delete', login_required(deletePostPage.as_view(),login_url='login'), name='deletePost'),
    path('glossary', views.glossaryPage, name='glossary'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', login_required(views.logoutUser, login_url='login'), name='logout')
]
