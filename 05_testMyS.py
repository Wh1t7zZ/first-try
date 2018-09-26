from Mysqlpython import *

mysql=Mysqlpython("db4")
sql_select='select * from sheng;'
result=mysql.getall(sql_select)
print(result)