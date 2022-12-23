from django.shortcuts import render
from Lesson_12_Models_writers.models import *


# Create your views here.

def books(request):
    content = Book.objects.all()
    categories = Categorie.objects.all()
    return render(template_name="books.html", request=request, context={"content": content, "categories": categories})



def books_filter(request, categorie):
    content = Book.objects.filter(style__name=categorie)
    categories = Categorie.objects.all()
    return render(template_name="books.html", request=request, context={"content": content, "categories": categories})