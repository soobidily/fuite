from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField("Username", max_length=30)
    password = models.CharField("Password", max_length=24)
