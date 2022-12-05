from django.urls import path, include, re_path
from Lesson_6_writers.views import *


urlpatterns = {
    path("", home),
    path("writers", writers),
    path("top_best_books", top_best_books)
}