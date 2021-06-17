from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
"""
title – CharField with max-length of 20
pages – IntegerField with default value of 0
description – CharField with max length of 100 and empty string as a default value
author – CharField with max length of 20
"""


class Book(models.Model):
    title = models.CharField(
        max_length=20,
    )
    pages = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    description = models.CharField(
        max_length=100,
        default=""
    )
    author = models.CharField(
        max_length=20,
    )
