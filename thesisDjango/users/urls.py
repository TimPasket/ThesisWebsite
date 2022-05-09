from django.urls import path
from .views import homePage, postDetailsPage, addPostPage, editPostPage, deletePostPage
from .import views

urlpatterns = [
    path('', homePage.as_view(), name='home'),
    path('post/<int:pk>', postDetailsPage.as_view(), name='postDetails'),
    path('add-Post', addPostPage.as_view(), name='addPost'),
    path('post/edit/<int:pk>', editPostPage.as_view(), name='editPost'),
    path('post/<int:pk>/delete', deletePostPage.as_view(), name='deletePost'),
    path('glossary', views.glossaryPage, name='glossary'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout')
]
