from django.shortcuts import render, redirect
from web_basics_exam.web_basics_exam.main_app.views.core_views import get_profile


def home(req):
    temp = ''
    profile = get_profile()
    if not profile:
        return redirect('create_profile')
    context = {
        '': '',

    }
    return render(req, temp, context)
