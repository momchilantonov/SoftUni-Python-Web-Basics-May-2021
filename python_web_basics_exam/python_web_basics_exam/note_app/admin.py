from django.contrib import admin

from python_web_basics_exam.note_app.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_url', 'content']
