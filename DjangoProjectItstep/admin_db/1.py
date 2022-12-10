import pymysql

connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Maksuwa1488",
    database="django_one",
    cursorclass=pymysql.cursors.DictCursor

)
print("ok")
with connection.cursor() as cursor:
    cursor.execute(f"select photo from `table` where nameProduct = 'photo namber one'")
    base_64 = cursor.fetchone()
    print(base_64)