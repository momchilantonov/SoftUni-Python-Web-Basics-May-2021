from django.shortcuts import render


# Create your views here.
def index(req):
    context = {
        "list": "List of persons:",
    }
    return render(req, "index.html", context)
