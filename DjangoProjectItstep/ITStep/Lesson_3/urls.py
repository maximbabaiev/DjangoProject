from django.urls import path, include, re_path
from Lesson_3.views import *

urlpatterns = [
    path("home/", home),
    path("history/", history),
    path("history/1885/", france1885),
    path("cities/", cities),
    # re_path(r"^cities/paris/\w*$", paris),
    re_path("^cities/marseille/\w*$", marseille),
    path("cities/paris/1924", paris1924),
    path("facts/", facts_about_the_country)
]
