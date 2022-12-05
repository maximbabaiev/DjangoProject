from django.shortcuts import render


# Create your views here.


def main(request):
    return render(request, "main.html", )


def pers(request, name):
    star_wars = {

        "Luk": "Люк Скайуокер - один из главных персонажей вселенной 'Звездных Войн',"
               " джедай, сын сенатора с Набу Падме Амидалы и рыцаря-джедая Энакина Скайуокера",

        "Leia": "Лея Органа - дочь рыцаря-джедая Энакина Скауокера и сенатора Падме Амидалы Набери",

        "Khan": "Хан Соло - пилот косического корабля 'Сокол Тысячилетия',"
                " его бортмеханик и второй пилот Чубака"
    }

    return render(request, "luk.html", context=star_wars.get(name))
