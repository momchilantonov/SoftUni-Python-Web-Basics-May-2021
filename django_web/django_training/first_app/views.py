from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django_training.first_app.models import Person


def index(req):
    context = {
        "list": "List of persons:",
        "people": Person.objects.all()
    }
    return render(req, "index.html", context)


def list_phones(req):
    context = {
        "phones": [
            {"name": "IPhone 12", "quantity": 10},
            {"name": "Galaxy S20", "quantity": 0},
            {"name": "Xiaomi Redmi N5", "quantity": 20},
        ]
    }
    return render(req, "phones.html", context)


# def index_test(req):
# just show http response
# return HttpResponse("Test text", content_type="text")
# return HttpResponse({"name": "Momchil"}, content_type="application/json")

def create_person(req):
    Person(
        first_name="Peter",
        last_name="Ivanov",
        age=30,
        address="Varna"
    ).save()
    return redirect("/first_app")
