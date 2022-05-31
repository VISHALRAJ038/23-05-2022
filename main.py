#SQLite
import sqlite3
con = sqlite3.connect('marks.db')
query='''CREATE TABLE if not exists students(
         RollNo INT PRIMARY KEY,
         Name TEXT,
         Python TEXT,
         Maths TEXT
          )'''
con.execute(query)
con.commit()
query='''INSERT INTO students
         VALUES(?,?,?,?)'''
multiple_rows=[(1,'vinay','O','A'),(2,'vnay','A','A'),(3,'vi','O','A'),(4,'vy','A','A')]
cursor=con.cursor()
cursor.executemany(query,multiple_rows)
con.commit()
query='''SELECT* FROM students'''
cursor.execute(query)
all_rows=cursor.fetchall()
for row in all_rows:
  print(row)
query='''SELECT*FROM students WHERE Maths='A'
      '''
cursor.execute(query)
all_rows = cursor.fetchall()
for row in all_rows:
  print(row)