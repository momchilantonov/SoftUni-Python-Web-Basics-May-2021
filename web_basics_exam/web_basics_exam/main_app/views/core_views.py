from django.shortcuts import render, redirect
from web_basics_exam.web_basics_exam.main_app.models.note import Note
from web_basics_exam.web_basics_exam.main_app.models.profile import Profile


def get_profile():
    return Profile.objects.first()


def get_note_by_id(pk):
    return Note.objects.get(pk=pk)


def show_form(req, form, temp):
    context = {
        'form': form,
    }
    return render(req, temp, context)


def save_form(req, form, temp, red):
    if form.is_valid():
        form.save()
        return redirect(red)
    return show_form(req, form, temp)
