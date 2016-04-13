from pymysql import connect,err,sys,cursors
conn=connect("csmysql.cs.cf.ac.uk",user='c1512900',passwd='uWC3hneR',db='c1512900')
cursor=conn.cursor()
cursor.execute("SELECT * FROM TestResults")
data=cursor.fetchall()

def insert(Name, ID, TestID, Score):
	cursor.execute("INSERT INTO TestResults(Student_Name, Student_Number, Topic_ID, Test_Result) VALUES (%s, %s, %s, %s)", (Name, ID, TestID, Score))
	conn.commit()

