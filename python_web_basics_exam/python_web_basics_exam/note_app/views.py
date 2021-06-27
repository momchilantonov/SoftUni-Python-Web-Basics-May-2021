from django.shortcuts import render, redirect

from python_web_basics_exam.core_app.views import show_form, save_form, get_obj_by_pk
from python_web_basics_exam.note_app.forms import CreateNoteForm, EditNoteForm, DeleteNoteForm
from python_web_basics_exam.note_app.models import Note


def add_note(req):
    temp = 'note-create.html'
    red = 'home page'
    if req.method == "GET":
        form = CreateNoteForm()
        return show_form(req, temp, form)
    form = CreateNoteForm(req.POST)
    return save_form(req, temp, red, form)


def edit_note(req, pk):
    temp = 'note-edit.html'
    red = 'home page'
    note = get_obj_by_pk(Note, pk)
    if req.method == "GET":
        form = EditNoteForm(initial=note.__dict__)
        return show_form(req, temp, form)
    form = EditNoteForm(
        req.POST,
        instance=note,
    )
    return save_form(req, temp, red, form)


def delete_note(req, pk):
    temp = 'note-delete.html'
    red = 'home page'
    note = get_obj_by_pk(Note, pk)
    if req.method == "GET":
        form = DeleteNoteForm(initial=note.__dict__)
        return show_form(req, temp, form)
    note.delete()
    return redirect(red)


def details_note(req, pk):
    temp = 'note-details.html'
    note = get_obj_by_pk(Note, pk)
    context = {
        'note': note,
    }
    return render(req, temp, context)


def get_notes_count(obj):
    return obj.count()
