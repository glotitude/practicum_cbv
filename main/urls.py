from django.contrib import admin
from django.urls import path

from .views import NotesView

urlpatterns = [
    path('notes/', NotesView.as_view()),
]
