from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def lets_do_it(request):
    return render(request, "indexwriters.html", context={
        "lets_do_it": [{
            "priority": 100,
            "task": "Составить список дел"
        }, {
            "priority": 150,
            "task": "Изучать Django"
        }, {
            "priority": 1,
            "task": "Думать о смысле жизни"
        }]
    })
