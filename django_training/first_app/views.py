from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_training.first_app.models import Person


def index(req):
    context = {
        "list": "List of persons:",
        "people": Person.objects.all()
    }
    return render(req, "index.html", context)


def list_phones(req):
    # just show http
    # return HttpResponse("Phone list")
    context = {
        "phones": [
            {"name": "IPhone 12", "quantity": 10},
            {"name": "Galaxy S20", "quantity": 0},
            {"name": "Xiaomi Redmi N5", "quantity": 20},
        ]
    }
    return render(req, "phones.html", context)
