import pymysql

db=pymysql.connect(host='localhost',user='root',
                   passwd='123456',db='db4',charset='utf8')

cursor=db.cursor()

try:
    s_name=input('请输入省份:')
    s_id=input('请输入该省编号:')
    sql_insert='insert into sheng(s_name,s_id) values(%s,%s);'
    cursor.execute(sql_insert,[s_name,s_id])
    db.commit()
    print("ok")
except Exception as e:
    db.rollback()
    print('Failed',e)

cursor.close()
db.close()