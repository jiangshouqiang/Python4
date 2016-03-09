import pymysql

conn = pymysql.connect(user='root',password='jiangshouqiang',database='heritrex')
cursor = conn.cursor()

# cursor.execute('create table python(id varchar(20))')
cursor.execute('insert into python (id) values(%s)',['1'])
print(cursor.rowcount)
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from python')
values = cursor.fetchall()
print(values)