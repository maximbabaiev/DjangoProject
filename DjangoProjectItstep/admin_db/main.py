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
        # create_table = "create table `table_books` " \
        #                "(id int auto_increment, nameBook varchar(300),author varchar(300), yearCreate DATE, style varchar(30), publishingHouse varchar(30), availability BOOLEAN, photo MEDIUMTEXT, primary key (id))"
        create_table = f"insert into `table_books` (nameBook, author, yearCreate, style, publishingHouse, availability, photo) values " \
                       f"('Час Презрения','Анжей Сапковский', '1995-01-01', 'фентези', 'superNOWA', '1', '{basePhoto('images/Час презрения.png')}')"
        cursor.execute(create_table)
        connection.commit()



except Exception as ex:
    print(ex)
