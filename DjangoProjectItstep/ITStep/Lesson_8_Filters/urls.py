from django.urls import path, include, re_path
from Lesson_8_Filters.views import *


urlpatterns = [
    path('dictsort/', dictsort)
]