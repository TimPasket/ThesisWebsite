from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.shortcuts import redirect
from django.urls import reverse


class Post(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField()

  def __str__(self):
      return self.title + ' | ' + str(self.author)
  
  def get_absolute_url(self):
      return reverse("postDetails", args=(str(self.id)))

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    