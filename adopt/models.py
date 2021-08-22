from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class ClientTable(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20,blank=True)
    gender = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.user.username

class ChildRegTable(models.Model):

    fname=models.CharField(max_length=20,blank=False)
    lname=models.CharField(max_length=20,blank=False)
    contact = models.CharField(max_length=20,blank=False)
    gender = models.CharField(max_length=20,blank=False)
    address = models.CharField(max_length=30,blank=False)
    cname=models.CharField(max_length=20,blank=False)
    fname=models.CharField(max_length=20,blank=False)
    age=models.CharField(max_length=20,blank=False)
    health=models.CharField(max_length=20,blank=False)
    height=models.CharField(max_length=20,blank=False)
    weight=models.CharField(max_length=20,blank=False)
    gender=models.CharField(max_length=20,blank=False)
    bloodgrp=models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.name
