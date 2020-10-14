# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(max_length = 900, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=30, blank=True)
    amount = models.IntegerField(blank=True, null=True)

class Transaction(models.Model):
    last_transaction =  models.IntegerField(default=00)
    name = models.CharField(max_length=30)
    reference = models.CharField(max_length=30)
    status = models.CharField(max_length=30, default='pending')
    sort_code = models.IntegerField(default=0000)
    account_number = models.CharField(max_length=30,null=True)
    date = models.DateTimeField(null=True)
    def __str__(self):
        return f"{self.name}"

class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    Email = models.EmailField(max_length=200)
    Telephone = models.CharField(max_length=200)
    Message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """String for representing the Model object."""
        return f"{self.name}"
