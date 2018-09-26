from pymysql import *

class Mysqlpython(object):
    """docstring for Mysqlpython"""
    def __init__(self,database,host='localhost',user='root',passwd='123456',
        port=3306,charset='utf8'):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.charset=charset
        self.port=port
        self.database=database

        
    def open(self):
        self.conn=connect(host=self.host,user=self.user,passwd=self.passwd,
            charset=self.charset,db=self.database,port=self.port)
        self.cur=self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

#执行SQL语句
    def workon(self,sql,L=[]):
        self.open()
        try:
            self.cur.execute(sql,L)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("failed",e)
        self.close()

#getall方法
    def getall(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        result=self.cur.fetchall()
        self.close()
        return result
        

#if __name__=='__main__':
 #   mysql=Mysqlpython("db4")
    #sql_insert='insert into sheng(s_name) values("河北省")'
    #workon(sql_insert)
  #sql_select='select * from sheng;'
#result=mysql.getall(sql_select)
#print(result)