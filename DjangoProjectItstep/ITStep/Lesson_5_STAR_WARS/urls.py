from django.urls import path, include, re_path
from Lesson_5_STAR_WARS.views import *


urlpatterns = [
    path('home/', main),
    path('home/<srt:name>', pers)
]