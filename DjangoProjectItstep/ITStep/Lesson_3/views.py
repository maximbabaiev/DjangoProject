from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, "indexHistory.html", context={
        'pagelist': [('history', 'История'), ('cities', 'Города'),
                     ('facts', 'Факты про страну')]})


def history(request):
    return render(request, 'indexHistory.html', context={
        'pagelist': [
            ('home', 'Главная'),
            ('cities', 'Города'),
            ('facts', 'Факты про страну')
        ]
    })


def cities(request):
    return render(request, 'indexHistory.html', context={
        'pagelist': [
            ('home', 'Главная'),
            ('history', 'История'),
            ('facts', 'Факты про страну')
        ]
    })


def facts_about_the_country(request):
    return render(request, 'indexHistory.html', context={
        'pagelist': [
            ('home', 'Главная'),
            ('history', 'История'),
            ('cities', 'Города')
        ]
    })


def paris(request):
    return HttpResponse(
        f"Paris<br><ul><li><a href = 'http://127.0.0.1:8000/cities/paris'>https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%B8%D0%B6</a><li><a href = 'http://127.0.0.1:8000/home'>HOME</a></li></li></ul></div>")


def marseille(request):
    return HttpResponse(
        f"Marseille<br><ul><li><a href = 'http://127.0.0.1:8000/cities/marseille'>https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%80%D1%81%D0%B5%D0%BB%D1%8C</a><li><a href = 'http://127.0.0.1:8000/home'>HOME</a></li></li></ul></div>")


def france1885(request):
    return HttpResponse(
        f"1885<br><ul><li><a href = 'http://127.0.0.1:8000/cities/marseille'>https://ru.frwiki.wiki/wiki/1885_en_France</a><li><a href = 'http://127.0.0.1:8000/home'>HOME</a></li></li></ul></div>")


def paris1924(request):
    return HttpResponse(
        f"Paris in 1924<br><ul><li><a href = 'http://127.0.0.1:8000/cities/paris/1924'>https://ru.wikipedia.org/wiki/%D0%9B%D0%B5%D1%82%D0%BD%D0%B8%D0%B5_%D0%9E%D0%BB%D0%B8%D0%BC%D0%BF%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B5_%D0%B8%D0%B3%D1%80%D1%8B_1924</a><li><a href = 'http://127.0.0.1:8000/home'>HOME</a></li></li></ul></div>")
