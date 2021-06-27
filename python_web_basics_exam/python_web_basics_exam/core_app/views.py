from django.shortcuts import render, redirect

from python_web_basics_exam.note_app.models import Note
from python_web_basics_exam.profile_app.forms import CreateProfileForm
from python_web_basics_exam.profile_app.models import Profile


def get_obj(obj):
    return obj.objects.first()


def get_all_objs(obj):
    return obj.objects.all()


def get_obj_by_pk(obj, pk):
    return obj.objects.get(pk=pk)


def show_form(req, temp, form):
    context = {
        'form': form,
    }
    return render(req, temp, context)


def save_form(req, temp, red, form):
    if form.is_valid():
        form.save()
        return redirect(red)
    return show_form(req, temp, form)


def home_page_with_profile(req):
    temp = 'home-with-profile.html'
    profile = get_obj(Profile)
    notes = get_all_objs(Note)
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(req, temp, context)


def home_page_without_profile(req):
    temp = 'home-no-profile.html'
    red = 'home page'
    if req.method == 'GET':
        form = CreateProfileForm()
        return show_form(req, temp, form)
    form = CreateProfileForm(req.POST)
    return save_form(req, temp, red, form)


def home_page(req):
    profile = get_obj(Profile)
    if profile:
        return home_page_with_profile(req)
    return home_page_without_profile(req)
