from django import forms

from python_web_basics_exam.note_app.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'row': 3,
                    'style': 'resize: none',
                }
            ),
        }


class CreateNoteForm(NoteForm):
    pass


class EditNoteForm(NoteForm):
    pass


class DeleteNoteForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
