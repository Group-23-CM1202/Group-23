from pymysql import connect,err,sys,cursors
conn=connect("csmysql.cs.cf.ac.uk",user='c1512900',passwd='uWC3hneR',db='c1512900')
cursor=conn.cursor()
cursor.execute("SELECT * FROM Lecturer")
data=cursor.fetchall()

myQuery ='INSERT INTO Lecturer VALUES (%s, %s, %s, %s)'	
cursor.execute(myQuery, ('Lecturer Name', 'Module', 'e-mail', 'Pass'))
conn.commit()
print(data)

