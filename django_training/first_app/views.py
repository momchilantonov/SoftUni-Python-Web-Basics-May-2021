from django.shortcuts import render

# Create your views here.
from django_training.first_app.models import Person


def index(req):
    context = {
        "list": "List of persons:",
        "people": Person.objects.all()
    }
    return render(req, "index.html", context)
