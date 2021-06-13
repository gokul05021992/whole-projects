import pymysql.cursors
from pymysql import *

connection=pymysql.connect(host='localhost',user='root',password='',db='student',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql="update details set name='jaya' where id=101" #update table_name set update_detail where condition
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()