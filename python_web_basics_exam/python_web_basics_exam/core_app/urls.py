from django.urls import path

from python_web_basics_exam.core_app.views import home_page

urlpatterns = [
    path('', home_page, name='home page'),
]