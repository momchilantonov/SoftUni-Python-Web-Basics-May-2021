from django.contrib import admin
# from web_basics_exam.web_basics_exam.main_app.models import 'model'


@admin.register('model')
class Admin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    sortable_by = []
