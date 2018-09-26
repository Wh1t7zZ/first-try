from Mysqlpython import Mysqlpython
from hashlib import sha1

username=input('请输入用户名：')
password=input('请输入密码：')

#加密
s1=sha1()#创sha1加密对象爱嗯
s1.update(password.encode('utf-8'))
password2=s1.hexdigest() #返回十六进制加密结果

#和数据库中表记匹配
mysql=Mysqlpython('db4')
sql_select='select password from user where username=%s;'
result=mysql.getall(sql_select,[username])


if len(result) ==0:
    print("用户名不存在！")
elif result[0][0] == password2:
    print('登录成功0.0')
else:
    print('密码错误！')