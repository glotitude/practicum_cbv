from django.contrib import admin
from django.urls import path

from .views import NotesView, NotesTemplate

urlpatterns = [
    path('notes/', NotesView.as_view()),
    path('notes/list/', NotesTemplate.as_view()),
]
