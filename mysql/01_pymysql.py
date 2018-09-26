import pymysql

#1.创建数据库链接对象

db = pymysql.connect(host="localhost", user="root",
    passwd="123456", db="db4",charset="utf8")
#2.利用db# 创建游标对象
cursor = db.cursor()
#利用cursor的execute()执行SQL命令
cursor.execute('insert into sheng values(30,400000,"吉林省");')
#提交到数据库执行
db.commit()
print('ok')
#关闭游标对象
cursor.close()
#断开数据库连接
db.close()