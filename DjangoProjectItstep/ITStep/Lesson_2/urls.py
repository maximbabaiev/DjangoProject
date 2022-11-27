from django.urls import path, include, re_path
from Lesson_2.views import home, news, management, city_leaders, facts_about_the_city, contactPhones

urlpatterns = [
    path("", home),
    re_path(r"^news/\w*$", news),
    re_path("^management/\w*$", management),
    re_path("^cityleaders/\w*$", city_leaders),
    re_path("^fact sabout the city/\w*$", facts_about_the_city),
    re_path("^contactPhones/\w*$", contactPhones),

]


