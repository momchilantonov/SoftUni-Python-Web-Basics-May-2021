from django.contrib import admin
from django.urls import path

from django_training.first_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index)
]
