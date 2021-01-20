#encoding:utf-8
import ConfigParser

cf = ConfigPaser.ConfigPaser()
#host user pass port
cf.read("database.conf")
db_host = cf.get("db","db.host")
db_port = cf.get("db","db.port")
db_user = cf.get("db","db_user")
db_pass = cf.get("db","db.pass")
db_db   = cf.get("db","db_db")

#sql动作

#查询待办列表
sqltodo = "select a.* b.* from `task` where assginee = 'xxx' and "

#查询已办列表

sqldone = "select * from task where assginee = 'xxx' and status='2'"

def connect():
    #创建连接
    conn = MySQLdb.Connect(
        host=db_host, 
        port= db_port,
        user= db_user,
        passwd=db_pass,
        db=db_db, 
        charset='utf8',
    )

    #获取游标
    cur=conn.cursor()
    
    #查询接口
    sql = 'select * from where '
    
