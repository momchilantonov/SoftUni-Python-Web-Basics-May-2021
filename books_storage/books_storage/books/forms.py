from django import forms
from .models import Book

"""
title – TextInput with class form-control
pages – NumberInput with class form-control
author – TextInput with class form-control
description – Textarea with class form-control
"""


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'pages': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
