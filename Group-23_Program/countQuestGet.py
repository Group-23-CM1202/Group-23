from pymysql import connect, err, sys, cursors
from random import shuffle

conn = connect("csmysql.cs.cf.ac.uk", user = 'c1455582', passwd = 'jzgwyT8pK', db = 'c1455582')

cursor = conn.cursor()

cursor.execute("SELECT * FROM Counting_Test")
data = cursor.fetchall()

def getQuestion(number):
    number -= 1
    return ([i[number]for i in data][0])

def getCorrectAnswer(number):
    number -= 1
    return ([i[number]for i in data][1])

def getAnswersShuffled(number):
    number -= 1
    a = ([i[number]for i in data][1:])
    shuffle(a)
    return (a)


