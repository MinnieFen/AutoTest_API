# coding:utf-8
import MySQLdb
from config import readconfig
import ast
class MySQLUtil():
    def __init__(self,db):
        self.sql_info = {'host': readconfig.sql_host,
                    'user': readconfig.sql_uer,
                    'port': readconfig.sql_port,
                    'password': readconfig.sql_password,
                    'db': db,
                    'charset': readconfig.sql_charset}
        self.conn = MySQLUtil.__connect(self.sql_info)
    @staticmethod    # 声明静态方法，调用该函数时不需要实例化
    def __connect(sql_info):
        try:
            conn = MySQLdb.connect(host = sql_info['host'],
                                   user = sql_info['user'],
                                   port = int(sql_info['port']),
                                   password = sql_info['password'],
                                   db = sql_info['db'],
                                   charset = sql_info['charset'])
            return conn
        except Exception as a:
            print('数据库连接异常：%s' %a)
    # 执行sql
    def get_execute(self,sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
        except Exception as a:
            self.conn.rollback()
            print('执行SQL异常：%s' %a)
        else:
            self.conn.commit()
            rows = cursor.fetchall()
            cursor.close()
            return rows
    # 获取执行sql的数据
    def get_rows(self,sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
        except Exception as a:
            print('执行SQL异常:%s' %a)
        else:
            self.conn.commit()
            rows = cursor.fetchall()
            cursor.close()
            return rows
    # 查询数据库
    def select(self,search,table,where):
        search_list = ast.literal_eval(search)         # 将从excel获取的字符串转换成list
        sql_search = ','.join(search_list)             # search_list 的类型需要为list
        sql = 'select %s from %s where %s;' %(sql_search,table,where)
        return self.get_execute(sql)
    # 更新数据库
    def update(self,table,set,where):
        sql = 'update %s set %s where %s;' %(table,set,where)
        return self.get_execute(sql)
    # 关闭数据库连接
    def mysql_close(self):
        try:
            self.conn.close()
        except Exception as a:
            print('关闭数据库异常：%s' %a)