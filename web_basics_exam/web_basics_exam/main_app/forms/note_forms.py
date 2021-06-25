from django import forms
from web_basics_exam.web_basics_exam.main_app.models.note import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class CreateNoteForm(NoteForm):
    pass


class EditNoteForm(NoteForm):
    pass


class DeleteNoteForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

