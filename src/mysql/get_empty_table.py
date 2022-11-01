# *-* coding:utf-8 *-
import pymysql


#plisp
# host = '127.0.0.1';
# port = 3306
# user = 'root'
# passwd = '123456'
# db = 'plisp'
# charset = 'utf8'

connection = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor= connection.cursor()
try:
    execute = cursor.execute("show tables;")
    fetchall = cursor.fetchall()
    for i in fetchall:
        for j in i:
            sql=" select * from "+j
            cursor_execute = cursor.execute(sql)
            cursor_fetchall = cursor.fetchall()
            #print(cursor_fetchall)
            for k in cursor_fetchall:
                for l in k:
                    if(l==0):
                        print(j)

finally:
    cursor.close()
    connection.close()





