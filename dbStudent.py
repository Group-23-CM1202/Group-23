from pymysql import connect,err,sys,cursors
conn=connect("csmysql.cs.cf.ac.uk",user='c1512900',passwd='uWC3hneR',db='c1512900')
cursor=conn.cursor()
cursor.execute("SELECT * FROM Student")
data=cursor.fetchall()

myQuery ='INSERT INTO Student VALUES (%s, %s, %s, %s)'	
cursor.execute(myQuery, ('Student Name', 'Student Number', 'email', 'Pass'))
conn.commit()
print(data)

