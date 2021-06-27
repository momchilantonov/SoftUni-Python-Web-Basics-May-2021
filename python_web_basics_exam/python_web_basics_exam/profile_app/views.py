from django.shortcuts import render, redirect

from python_web_basics_exam.core_app.views import get_obj, get_all_objs
from python_web_basics_exam.note_app.models import Note
from python_web_basics_exam.note_app.views import get_notes_count
from python_web_basics_exam.profile_app.models import Profile


def details_profile(req):
    temp = 'profile.html'
    red = 'delete profile'
    profile = get_obj(Profile)
    notes = get_all_objs(Note)
    notes_count = get_notes_count(notes)
    context = {
        'profile': profile,
        'notes_count': notes_count
    }
    if req.method == "GET":
        return render(req, temp, context)
    return redirect(red)


def delete_profile(req):
    red = 'home page'
    profile = get_obj(Profile)
    notes = get_all_objs(Note)
    profile.delete()
    for note in notes:
        note.delete()
    return redirect(red)
