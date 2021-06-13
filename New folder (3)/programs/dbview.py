import pymysql.cursors
from pymysql import *
connection=pymysql.connect(host='localhost',user='root',password='',db='hr',charset='utf8mb4',cursorclass=pymysql.cursors.Cursor)
try:
    with connection.cursor() as cursors:
        sql="select * from staff"
        cursors.execute(sql)
        result=cursors.fetchall()
        print(result)
        connection.commit()
finally:
    connection.close()