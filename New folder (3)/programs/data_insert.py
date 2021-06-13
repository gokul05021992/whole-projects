import pymysql.cursors
from pymysql import *

connection=pymysql.connect(host='localhost',user='root',password='',db='student',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql="insert into `details` values(102,'kavi')"
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()