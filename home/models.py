from django.db import models


class Volunteer(models.Model):
    """ Model for Volunteers """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    about = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Animal(models.Model):
    """ Model for Animals"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    type = models.CharField(max_length=254)
    breed = models.CharField(max_length=254, null=True, blank=True)
    about = models.TextField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    """ Model for Contact form """
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    question = models.TextField(max_length=400)

    def __str__(self):
        return self.email
