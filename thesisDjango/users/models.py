from django.db import models

# Create your models here.

class userAccounts(models.Model):
  userNname = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)
  dateCreated = models.DateTimeField(auto_now_add=True)
  role = models.CharField(max_length=200, default='subscriber')