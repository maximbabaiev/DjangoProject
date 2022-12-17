from django.shortcuts import render
from Lesson_12_Models_writers.models import Book


# Create your views here.

def books(request):
    content = Book.objects.all()
    return render(template_name="books.html", request=request, context={"content": content})
