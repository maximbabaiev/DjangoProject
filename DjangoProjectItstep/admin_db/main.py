import pymysql
from django.shortcuts import render
import base64


def basePhoto(path):
    with open(path, "rb") as file:
        base_64 = base64.b64encode(file.read()).decode("utf-8")
    return base_64


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
        # create_table = "create table `table` " \
        #                "(id int auto_increment, nameProduct varchar(300),urlProduct varchar(300), photo MEDIUMTEXT, primary key (id))"
        create_table = f"insert into `table` (nameProduct, urlProduct, photo) values " \
                       f"('Monitor_2','https://hard.rozetka.com.ua/ua/asus_90lm05b0_b01170/p251340976/' ,'{basePhoto('images/img_1.png')}')"
        cursor.execute(create_table)
        connection.commit()

except Exception as ex:
    print(ex)
