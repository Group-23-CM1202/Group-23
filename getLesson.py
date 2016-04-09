from pymysql import connect, err, sys, cursors



conn = connect("csmysql.cs.cf.ac.uk", user = 'c1455582', passwd = 'jzgwyT8pK', db = 'c1455582')

cursor = conn.cursor()

cursor.execute("SELECT * FROM Lessons")
data = cursor.fetchall()

def getLessonID(ID):
    ID -= 1
    return (data[ID][0])


def getLessonName(ID):
    ID -= 1
    return (data[ID][1])


def getLessonContent(ID):
    ID -= 1
    part = data[ID][2].split(' ')
    return (part)

