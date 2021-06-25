from django.shortcuts import render, redirect
from web_basics_exam.web_basics_exam.main_app.forms.note_forms import CreateNoteForm, EditNoteForm, DeleteNoteForm
from web_basics_exam.web_basics_exam.main_app.views.core_views import show_form, save_form, get_note_by_id


def create_note(req):
    temp = ''
    red = 'home'
    if req.method == "GET":
        form = CreateNoteForm()
        return show_form(req, form, temp)
    form = CreateNoteForm(req.POST)
    return save_form(req, form, temp, red)


def edit_note(req, pk):
    temp = ''
    red = 'home'
    note = get_note_by_id(pk)
    if req.method == "GET":
        form = EditNoteForm(initial=note.__dict__)
        return show_form(req, form, temp)
    form = EditNoteForm(
        req.POST,
        instance=note,
    )
    return save_form(req, form, temp, red)


def delete_note(req, pk):
    temp = ''
    red = 'home'
    note = get_note_by_id(pk)
    if req.method == "GET":
        form = DeleteNoteForm(initial=note.__dict__)
        # for _, field in form.fields.items():
        #     field.widget.attrs['disabled'] = True
        # form.save(commit=False)
        return show_form(req, form, temp)
    note.delete()
    return redirect(red)


def details_note(req, pk):
    temp = ''
    note = get_note_by_id(pk)
    context = {
        'note': note,
    }
    return render(req, temp, context)
