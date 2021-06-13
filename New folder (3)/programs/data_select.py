import pymysql.cursors
from pymysql import *
connection=pymysql.connect(host='localhost',user='root',password='',db='student',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursors:
        sql="select * from details"
        cursors.execute(sql)
        result=cursors.fetchall()
        print(result)
        connection.commit()
finally:
    connection.close()