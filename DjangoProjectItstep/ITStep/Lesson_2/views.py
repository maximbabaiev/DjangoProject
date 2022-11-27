from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, "index.html", context={"text": 'hello world', 'pagelist': ['news', 'management', 'cityleaders', 'fact sabout the city', 'contactPhones']})


def news(request):
    return HttpResponse(f"NEWS<br><div><ul><li><a href = 'http://127.0.0.1:8000'>HOME</a></li></ul></div>")


def management(request):
    return HttpResponse(f"MANAGEMENT<br><div><ul><li><a href = 'http://127.0.0.1:8000'>HOME</a></li></ul>")


def city_leaders(request):
    return HttpResponse(f"city leaders<br><div><ul><li><a href = 'http://127.0.0.1:8000'>HOME</a></li></ul>")


def facts_about_the_city(request):
    return HttpResponse(f"facts about the city<br><div><ul><li><a href = 'http://127.0.0.1:8000'>HOME</a></li></ul>")


def contactPhones(request):
    return HttpResponse(f"contactPhones<br><div><ul><li><a href = 'http://127.0.0.1:8000'>HOME</a></li></ul>")
