import pymysql.cursors
from pymysql import *
con=pymysql.connect(host='localhost',user='root',password='',db='employee',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
try:
    with con.cursor() as cursor:
        sql="insert into `employee name` values('gokul',101)"
        cursor.execute(sql)
        con.commit()
finally:
       con.close

