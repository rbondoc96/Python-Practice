from django.urls import path

from .question import get_all

urlpatterns = [
    path("questions/", get_all,)
]