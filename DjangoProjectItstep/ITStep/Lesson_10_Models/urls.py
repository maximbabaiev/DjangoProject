from django.urls import path, include, re_path
from Lesson_9_DB_image.views import *


urlpatterns = [
    path('', image),
    path('product/', product)
]