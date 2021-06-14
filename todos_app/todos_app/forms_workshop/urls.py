from django.urls import path
from .views import show_form_data

urlpatterns = [
    path('', show_form_data, name='show form'),
]
