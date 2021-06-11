from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("first_app/", include("django_training.first_app.urls")),
    path("people/", include("django_training.people.urls")),
]
