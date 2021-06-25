from django.contrib import admin
from web_basics_exam.web_basics_exam.main_app.models.note import Note
from web_basics_exam.web_basics_exam.main_app.models.profile import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    sortable_by = []


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    sortable_by = []
