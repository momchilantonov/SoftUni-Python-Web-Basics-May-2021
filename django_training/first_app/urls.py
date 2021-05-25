from django.urls import path
from django.views.generic import TemplateView

from django_training.first_app.views import index, list_phones

urlpatterns = [
    path("test/", index),
    path("phones/", list_phones),
    # Show template without write a func in view.py (show html page without python logic)
    # path("phones2/", TemplateView.as_view(template_name="phones.html")),
]
