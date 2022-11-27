from django.contrib import admin
from django.urls import path, include, re_path
from Lesson_1.views import first_views, second_views, num, sum, db, add_product, selectFromAcademy, select_year,\
   old_year, email, phone_num

urlpatterns = [
   path('first/', first_views),
   path('second/<str:name>/', second_views),
   path('second/<int:num_>', num),
   path('summa/<int:a> <int:b>', sum),
   path('base/<str:name>', db),
   path('iserttobase/<str:name> <str:dean>', add_product),
   path('select/<str:name>', selectFromAcademy),
   # re_path(r'^year/(?P<year>\d+)$', select_year),
   # re_path(r'^year/(?P<year>\d+.?\d{2})$', select_year),
   re_path(r'^year/(?P<year>19[1-9]\d?)$', old_year),
   re_path(r'^email/(?P<email>[a-zA-Z\d]+@[a-z\d.-]+\.[a-z]{2,4})$', email),
   re_path(r'^phone/(?P<phone>\+(\d){12})$', phone_num)
]