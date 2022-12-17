"""ITStep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('Lesson_1/', include('Lesson_1.urls')),
    # path('', include('Lesson_2.urls')),
    # path('', include('Lesson_3.urls')),
    # path("", include("Lesson_4.urls"))
    # path('', include("Lesson_5_STAR_WARS.urls"))
    # path('', include("Lesson_6_writers.urls"))
    # path('', include("Lesson_7_library.urls"))
    # path('Lesson_8/', include('Lesson_8_Filters.urls'))
    # path("Lesson/", include("Lesson_8_DB.urls"))
    # path('', include("Lesson_9_DB_image.urls")),
    # path('', include("Lesson_10_Models.urls"))
    # path('', include("Lesson_11_Models.urls"))
    path('', include("Lesson_12_Models_writers.urls"))
]
