from django.urls import path
from .views import index, create_todo

urlpatterns = [
    path('', index, name='index'),
    path('create', create_todo, name='create_todo'),
    # path('todos-add/', create_todo),
    # path('todo-change-state/<int:pk>', change_todo_state),
]
