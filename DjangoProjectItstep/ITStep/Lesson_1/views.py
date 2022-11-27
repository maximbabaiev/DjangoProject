from django.shortcuts import render
from django.http import HttpResponse
import pymysql


# Create your views here.
def select_year(request, year):
    return HttpResponse(f"{year}")


def old_year(response, year):
    return HttpResponse(year)


def email(request, email):
    return HttpResponse(email)


def phone_num(request, phone):
    return HttpResponse(phone)


def first_views(request):
    return HttpResponse("Hello world!")


def second_views(request, name):
    return HttpResponse(f"Hello {name}")


def num(request, num_):
    if num_ % 2 == 0:
        return HttpResponse(f"Это {num_} чет")
    else:
        return HttpResponse(f"Это {num_} не чет")


def sum(request, a, b):
    return HttpResponse(f"{a + b}")


def db(request, name):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user='root',
            password='Maksuwa1488',
            database="hospital",
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                select = f"select * from `{name}`"
                cursor.execute(select)
                result = cursor.fetchall()
                result_str = "<li>".join([f'{elem.get("id")}, {elem.get("name")}, {elem.get("Severity")}'
                                          for elem in result])

        finally:
            connection.close()
    except Exception as ex:
        print(ex)
    return HttpResponse(f"'Select all from db' - <ul><li>{result_str}</ul>")


def add_product(request, name, dean):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user='root',
            password='Maksuwa1488',
            database="academy",
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                select = f"insert into  `faculties` (Name, Dean) " \
                         f"values ('{name}', '{dean}')"
                cursor.execute(select)
                connection.commit()

        finally:
            connection.close()
    except Exception as ex:
        print(ex)
    return HttpResponse()


def selectFromAcademy(reqwest, name):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user='root',
            password='Maksuwa1488',
            database="academy",
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                select = f"select * from `{name}`"
                cursor.execute(select)
                result = cursor.fetchall()
                result_str = "<li>".join([f'{elem.get("id")}, {elem.get("Name")}, {elem.get("Dean")}'
                                          for elem in result])

        finally:
            connection.close()
    except Exception as ex:
        print(ex)
    return HttpResponse(f"'Select all from db' - <ul><li>{result_str}</ul>")
