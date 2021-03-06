from django.urls import path
from .views import index, create_book, edit_book

urlpatterns = [
    path("", index, name="index"),
    path("create/", create_book, name="create"),
    path("edit/<int:pk>", edit_book, name="edit"),
]
