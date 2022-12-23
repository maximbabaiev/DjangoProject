from django.urls import path, include, re_path
from Lesson_13_Model_CSV.views import *


urlpatterns = [
    path('up/', upload_data)
]