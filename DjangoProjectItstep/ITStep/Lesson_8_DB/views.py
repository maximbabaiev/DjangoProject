from django.shortcuts import render
import pymysql


# Create your views here.

def dateb(request):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Maksuwa1488",
            database="academy",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("ok")
        try:
            with connection.cursor() as cursor:
                select_all = "select * from academy.departments"
                cursor.execute(select_all)
                result = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex:
        print(ex)
    return render(request, "d_b.html", context={"result": result})
