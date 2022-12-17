from django.urls import path, include, re_path
from Lesson_12_Models_writers.views import *


urlpatterns = [
    path("books/", books)
]