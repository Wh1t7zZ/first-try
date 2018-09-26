import pymysql

db=pymysql.connect(host='localhost',user='root',passwd='123456',db='db4',charset='utf8')

cursor=db.cursor()

cursor.execute('insert into sheng(s_name) values("湖北省");')
cursor.execute('delete from sheng where id =8;')
cursor.execute('update sheng set s_name="浙江省" where id =1;')
db.commit()
cursor.close()
db.close()