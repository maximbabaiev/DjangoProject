from django.shortcuts import render


# Create your views here.


def home(request):
    choice_list = {
        "choice_list": [(
            "writers/", "Писатели"
        ), (
            "top_best_book/", "Топ лучших книг"
        )]
    }
    return render(request, "writers.html", context=choice_list)


def writers(reqwest):
    writers_list = {
        "choice_list": [(
            "", "Главная"
        ), (
            "top_best_book/", "Топ лучших книг"
        )],
        "writers": [(
            "r_salvatore", "Робберт Сальваторе"
        ), (
            "a_pehov", "Алексей Пехов"
        ), (
            "a_sapkovskii", "Анжей Сапковский"
        )],
        "writers_all": "Писатели"
    }
    return render(reqwest, "writers.html", context=writers_list)


def top_best_books(request):
    top_best_books_list = {
        "choice_list": [(
            "", "Главная"
        ), (
            "writers/", "Писатели"
        )],
        "top_books": [{
            "author": "Анжей Сапковский", "book": [
                "Меч Предназначения"
            ]
        }, {
            "author": "Алексей Пехов", "book": [
                "Мастер снов"
            ]
        }]
    }
    return render(request, "writers.html", context={
        "choice_list": top_best_books_list.get("choice_list"),
        "top_books": top_best_books_list["top_books"]
    })
