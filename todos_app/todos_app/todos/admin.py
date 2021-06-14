from django.contrib import admin
from .models import Todo
from .models.todo import Person, Category


# Option 2
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
    list_filter = ['owner']
    sortable_by = ['text']

    # def has_change_permission(self, request, obj=None):
    #     return False


# Option 1
# admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)
