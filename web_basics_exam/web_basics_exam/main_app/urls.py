from django.urls import path
from web_basics_exam.web_basics_exam.main_app.views.home_views import home
from web_basics_exam.web_basics_exam.main_app.views.profile_views import details_profile, create_profile
from web_basics_exam.web_basics_exam.main_app.views.note_views import create_note, edit_note, delete_note, details_note


urlpatterns = [
    path('', home, name='home'),
    path('add/', create_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', details_note, name='details note'),
    path('profile/', details_profile, name='details profile'),
    path('create_profile/', create_profile, name='create profile'),

]
