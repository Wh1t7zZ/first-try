
from pymysql import connect

db=connect(host='localhost',user='root',
           passwd='123456',db='db4',charset='utf8',port=3306)

cursor=db.cursor()
cursor.execute('select * from sheng;')
#查询结果放在cursor中
data1=cursor.fetchone()
print(data1)
data2=cursor.fetchmany(3)
print(data2)
data3=cursor.fetchall()
print(data3)

cursor.close()
db.close()