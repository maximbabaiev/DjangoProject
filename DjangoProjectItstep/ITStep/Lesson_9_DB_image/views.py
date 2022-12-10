from django.shortcuts import render
import base64
import os.path
import pymysql


# Create your views here.


def image(request):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Maksuwa1488",
            database="django_one",
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            cursor.execute(f"select * from `table`")
            base_64 = cursor.fetchall()
            print(base_64)


    except Exception as ex:
        print(ex)
    return render(template_name="index_img_1.html", request=request,
                  context={"img": base_64})
