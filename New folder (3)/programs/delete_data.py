import pymysql.cursors
from pymysql import *

connection=pymysql.connect(host='localhost',user='root',password='',db='student',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql="delete from details where id=102"
        cursor.execute((sql))
        connection.commit()

finally:
    connection.close()