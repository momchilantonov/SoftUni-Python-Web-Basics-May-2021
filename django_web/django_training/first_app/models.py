from django.db import models
from django.forms import forms


class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField()
    address = models.CharField(max_length=60)
