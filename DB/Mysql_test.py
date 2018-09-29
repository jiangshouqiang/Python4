import pymysql
from datetime import datetime,timedelta,timezone


conn = pymysql.connect(host='192.168.11.193',user='hibabyadm',password='hibaby@)!&',database='hibaby_sit')
cursor = conn.cursor()

for i in range(1000,9000):
    now = datetime.now()
    timeStr = datetime.strftime(now,'%Y%m%d%H%M%S%s')
    id = timeStr[:-8]+ str(i)
    cursor.execute('insert into pay_refund_no (pay_no,refund_no) values(%s,%s)',['P'+id,'R'+id])
    print("running ... ")
    conn.commit()
cursor.close()
# cursor.execute('create table python(id varchar(20))')
# cursor.execute('insert into python (id) values(%s)',['1'])
# print(cursor.rowcount)
# conn.commit()
# cursor.close()
#
# cursor = conn.cursor()
# cursor.execute('select * from FINANCEINFO')
# values = cursor.fetchall()
# print(values)