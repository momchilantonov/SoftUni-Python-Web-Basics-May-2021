from django.contrib import admin
from django.urls import path, include

from django_training.first_app.views import index, list_phones

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("django_training.first_app.urls"))
]
