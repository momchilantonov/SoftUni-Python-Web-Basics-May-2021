from django.shortcuts import render
from web_basics_exam.web_basics_exam.main_app.forms.profile_forms import CreateProfileForm
from web_basics_exam.web_basics_exam.main_app.views.core_views import show_form, save_form, get_profile


def details_profile(req):
    temp = ''
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(req, temp, context)


def create_profile(req):
    temp = ''
    red = 'home'
    if req.method == "GET":
        form = CreateProfileForm()
        return show_form(req, form, temp)
    form = CreateProfileForm(req.POST)
    return save_form(req, form, temp, red)
