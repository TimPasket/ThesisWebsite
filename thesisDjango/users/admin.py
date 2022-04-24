from django.contrib import admin

# Register your models here.

from .models import userAccounts

admin.site.register(userAccounts)