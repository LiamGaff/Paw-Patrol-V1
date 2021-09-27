from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    Password = models.CharField(max_length=10)
