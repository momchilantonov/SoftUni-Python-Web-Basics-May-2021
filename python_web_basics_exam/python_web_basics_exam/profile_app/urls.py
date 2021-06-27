from django.urls import path

from python_web_basics_exam.profile_app.views import details_profile, delete_profile

urlpatterns = [
    path('', details_profile, name='details profile'),
    path('delete/', delete_profile, name='delete profile')
]
