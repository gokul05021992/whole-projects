import pymysql.cursors
from pymysql import *

connection= pymysql.connect(host='localhost',user='root',password='',db='organisation',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursors:
        sql="insert into `staff` values (110,'vi','IT',20000)"
        cursors.execute(sql)
        connection.commit()
finally:
    connection.close