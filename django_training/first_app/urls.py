from django.urls import path

from django_training.first_app.views import index, list_phones

urlpatterns = [
    path("test/", index),
    path("phones/", list_phones)
]
