import pymysql.cursors
from pymysql import *

connection= pymysql.connect(host='localhost',user='root',password='',db='organisation',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursors:
        sql="select * from staff where salary = 20000"
        cursors.execute((sql))
        v = cursors.fetchall()
        for i in v:
            print(i)
        connection.commit()
finally:
    connection.close