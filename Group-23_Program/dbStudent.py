from pymysql import connect,err,sys,cursors
conn=connect("csmysql.cs.cf.ac.uk",user='c1512900',passwd='uWC3hneR',db='c1512900')
cursor=conn.cursor()
cursor.execute("SELECT * FROM Student")
data=cursor.fetchall()


def insert(Name, ID, TestID):
    cursor.execute("INSERT INTO Student(Student_Name, Student_Number, Pass) VALUES (%s, %s, %s)", (Name, ID, TestID))
    conn.commit()
    data = cursor.fetchall()


def getStudentID():
    return [x[1] for x in data]


def getStudentName():
    return [x[0] for x in data]


def getStudentPassword(user):
    return ([x[2] for x in data][user])

