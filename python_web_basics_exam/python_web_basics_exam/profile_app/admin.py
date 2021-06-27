from django.contrib import admin

from python_web_basics_exam.profile_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'image_url']
