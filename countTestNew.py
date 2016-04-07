import tkinter as tk
import randomCountingQuestionGenerator as rQG
import countQuestGet as QG
from pymysql import connect, err, sys, cursors
from random import shuffle

conn = connect("csmysql.cs.cf.ac.uk", user = 'c1455582', passwd = 'jzgwyT8pK', db = 'c1455582')
cur = conn.cursor()

class testApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (User, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Submit):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("User")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

lessonName = '001'
User = ''
QA1 = ''
A1 = QG.getCorrectAnswer(1)
QA2 = ''
A2 = QG.getCorrectAnswer(2)
QA3 = ''
A3 = QG.getCorrectAnswer(3)
QA4 = ''
A4 = QG.getCorrectAnswer(4)
QA5 = ''
A5 = QG.getCorrectAnswer(5)
QA6 = ''
A6 = 'python'
QA7 = ''
A7 = 'python'
QA8 = ''
A8 = 'python'
QA9 = ''
A9 = 'python'
QA10 = ''
A10 = 'python'

i = 0


class User(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        top = tk.Frame(self)
        top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        L1 = tk.Label(self, text="Student ID")
        L1.pack(in_=top, side=tk.LEFT)
        self.username = tk.Entry(self, bd=5)
        self.username.pack(in_=top, side=tk.RIGHT)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        submit = tk.Button(self, text='Submit', command=self.submit)
        submit.pack(in_=bottom, side=tk.RIGHT)
        self.label = tk.Label(self)
        self.label.pack(in_=bottom, side=tk.RIGHT)


    def submit(self):
        global User
        ID = self.username.get()
        if len(ID) != 8:
            self.label.config(text="Invalid ID")
        elif (ID[1:]).isdigit() != True:
            self.label.config(text="Invalid ID")
        else:
            User = ID
            self.controller.show_frame("Q1")


class Q1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.QA = QG.getAnswersShuffled(1)
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(1))
        label.pack(side="top", fill="x", pady=10)
        self.intVar = tk.StringVar()
        self.intVar.set('python')
        R1 = tk.Radiobutton(self, text=str(self.QA[0]), variable=self.intVar, value=str(self.QA[0]))
        R1.pack(anchor=tk.W)
        R2 = tk.Radiobutton(self, text=str(self.QA[1]), variable=self.intVar, value=str(self.QA[1]))
        R2.pack(anchor=tk.W)
        R3 = tk.Radiobutton(self, text=str(self.QA[2]), variable=self.intVar, value=str(self.QA[2]))
        R3.pack(anchor=tk.W)
        R4 = tk.Radiobutton(self, text=str(self.QA[3]), variable=self.intVar, value=str(self.QA[3]))
        R4.pack(anchor=tk.W)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Next = tk.Button(self, text="Next", command=self.confirm)
        Next.pack(in_=bottom, side=tk.RIGHT)

    def confirm(self):
        global QA1
        QA1 = self.intVar.get()
        print (QA1)
        self.controller.show_frame("Q2")


class Q2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Q = QG.getQuestion(2)
        self.QA = QG.getAnswersShuffled(2)
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(2))
        label.pack(side="top", fill="x", pady=10)
        self.intVar = tk.StringVar()
        self.intVar.set('python')
        R1 = tk.Radiobutton(self, text=str(self.QA[0]), variable=self.intVar, value=str(self.QA[0]))
        R1.pack(anchor=tk.W)
        R2 = tk.Radiobutton(self, text=str(self.QA[1]), variable=self.intVar, value=str(self.QA[1]))
        R2.pack(anchor=tk.W)
        R3 = tk.Radiobutton(self, text=str(self.QA[2]), variable=self.intVar, value=str(self.QA[2]))
        R3.pack(anchor=tk.W)
        R4 = tk.Radiobutton(self, text=str(self.QA[3]), variable=self.intVar, value=str(self.QA[3]))
        R4.pack(anchor=tk.W)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Back = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame("Q1"))
        Next = tk.Button(self, text="Next", command=self.confirm)
        Next.pack(in_=bottom, side=tk.RIGHT)
        Back.pack(in_=bottom, side=tk.RIGHT)

    def confirm(self):
        global QA2
        QA2 = self.intVar.get()
        print(QA2)
        self.controller.show_frame("Q3")



class Q3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Q = QG.getQuestion(3)
        self.QA = QG.getAnswersShuffled(3)
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(3))
        label.pack(side="top", fill="x", pady=10)
        self.intVar = tk.StringVar()
        self.intVar.set('python')
        R1 = tk.Radiobutton(self, text=str(self.QA[0]), variable=self.intVar, value=str(self.QA[0]))
        R1.pack(anchor=tk.W)
        R2 = tk.Radiobutton(self, text=str(self.QA[1]), variable=self.intVar, value=str(self.QA[1]))
        R2.pack(anchor=tk.W)
        R3 = tk.Radiobutton(self, text=str(self.QA[2]), variable=self.intVar, value=str(self.QA[2]))
        R3.pack(anchor=tk.W)
        R4 = tk.Radiobutton(self, text=str(self.QA[3]), variable=self.intVar, value=str(self.QA[3]))
        R4.pack(anchor=tk.W)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Back = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame("Q2"))
        Next = tk.Button(self, text="Next", command=self.confirm)
        Next.pack(in_=bottom, side=tk.RIGHT)
        Back.pack(in_=bottom, side=tk.RIGHT)

    def confirm(self):
        global QA3
        QA3 = self.intVar.get()
        print(QA3)
        self.controller.show_frame("Q4")



class Q4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Q = QG.getQuestion(4)
        self.QA = QG.getAnswersShuffled(4)
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(4))
        label.pack(side="top", fill="x", pady=10)
        self.intVar = tk.StringVar()
        self.intVar.set('python')
        R1 = tk.Radiobutton(self, text=str(self.QA[0]), variable=self.intVar, value=str(self.QA[0]))
        R1.pack(anchor=tk.W)
        R2 = tk.Radiobutton(self, text=str(self.QA[1]), variable=self.intVar, value=str(self.QA[1]))
        R2.pack(anchor=tk.W)
        R3 = tk.Radiobutton(self, text=str(self.QA[2]), variable=self.intVar, value=str(self.QA[2]))
        R3.pack(anchor=tk.W)
        R4 = tk.Radiobutton(self, text=str(self.QA[3]), variable=self.intVar, value=str(self.QA[3]))
        R4.pack(anchor=tk.W)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Back = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame("Q3"))
        Next = tk.Button(self, text="Next", command=self.confirm)
        Next.pack(in_=bottom, side=tk.RIGHT)
        Back.pack(in_=bottom, side=tk.RIGHT)

    def confirm(self):
        global QA4
        QA4 = self.intVar.get()
        print(QA4)
        self.controller.show_frame("Q5")




class Q5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Q = QG.getQuestion(5)
        self.QA = QG.getAnswersShuffled(5)
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(5))
        label.pack(side="top", fill="x", pady=10)
        self.intVar = tk.StringVar()
        self.intVar.set('python')
        R1 = tk.Radiobutton(self, text=str(self.QA[0]), variable=self.intVar, value=str(self.QA[0]))
        R1.pack(anchor=tk.W)
        R2 = tk.Radiobutton(self, text=str(self.QA[1]), variable=self.intVar, value=str(self.QA[1]))
        R2.pack(anchor=tk.W)
        R3 = tk.Radiobutton(self, text=str(self.QA[2]), variable=self.intVar, value=str(self.QA[2]))
        R3.pack(anchor=tk.W)
        R4 = tk.Radiobutton(self, text=str(self.QA[3]), variable=self.intVar, value=str(self.QA[3]))
        R4.pack(anchor=tk.W)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Back = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame("Q4"))
        Next = tk.Button(self, text="Next", command=self.confirm)
        Next.pack(in_=bottom, side=tk.RIGHT)
        Back.pack(in_=bottom, side=tk.RIGHT)

    def confirm(self):
        global QA5
        QA5 = self.intVar.get()
        print(QA5)
        self.controller.show_frame("Q6")




class Q6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Q = rQG.pickRandQuestion()
        self.QA = (self.Q[3:])
        self.QAS = shuffle(self.QA)
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.Quest()
        label.pack(side="top", fill="x", pady=10)
        self.intVar = tk.StringVar()
        self.intVar.set('python')
        R1 = tk.Radiobutton(self, text=str(self.QA[0]), variable=self.intVar, value=str(self.QA[0]))
        R1.pack(anchor=tk.W)
        R2 = tk.Radiobutton(self, text=str(self.QA[1]), variable=self.intVar, value=str(self.QA[1]))
        R2.pack(anchor=tk.W)
        R3 = tk.Radiobutton(self, text=str(self.QA[2]), variable=self.intVar, value=str(self.QA[2]))
        R3.pack(anchor=tk.W)
        R4 = tk.Radiobutton(self, text=str(self.QA[3]), variable=self.intVar, value=str(self.QA[3]))
        R4.pack(anchor=tk.W)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Back = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame("Q5"))
        Next = tk.Button(self, text="Next", command=self.confirm)
        Next.pack(in_=bottom, side=tk.RIGHT)
        Back.pack(in_=bottom, side=tk.RIGHT)

    def confirm(self):
        global QA6
        global A6
        if self.Q[0] == "C":
            self.answer = rQG.comboAns(self.Q[1], self.Q[2])
        elif self.Q[0] == "P":
            self.answer = rQG.permAns(self.Q[1], self.Q[2])
        A6 = self.answer
        QA6 = self.intVar.get()
        print(QA6)
        print(A6)
        self.controller.show_frame("Q7")


    def Quest(self):
        if self.Q[0] == "C":
            self.strVar.set("C(" + str(self.Q[1]) + ", " + str(self.Q[2]) + ") = :")
        elif self.Q[0] == "P":
            self.strVar.set("P(" + str(self.Q[1]) + ", " + str(self.Q[2]) + ") = :")
        else:
            self.strVar.set("ERROR!!")


class Q7(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Q = rQG.pickRandQuestion()
        self.QA = (self.Q[3:])
        self.QAS = shuffle(self.QA)
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.Quest()
        label.pack(side="top", fill="x", pady=10)
        self.intVar = tk.StringVar()
        self.intVar.set('python')
        R1 = tk.Radiobutton(self, text=str(self.QA[0]), variable=self.intVar, value=str(self.QA[0]))
        R1.pack(anchor=tk.W)
        R2 = tk.Radiobutton(self, text=str(self.QA[1]), variable=self.intVar, value=str(self.QA[1]))
        R2.pack(anchor=tk.W)
        R3 = tk.Radiobutton(self, text=str(self.QA[2]), variable=self.intVar, value=str(self.QA[2]))
        R3.pack(anchor=tk.W)
        R4 = tk.Radiobutton(self, text=str(self.QA[3]), variable=self.intVar, value=str(self.QA[3]))
        R4.pack(anchor=tk.W)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Back = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame("Q6"))
        Next = tk.Button(self, text="Next", command=self.confirm)
        Next.pack(in_=bottom, side=tk.RIGHT)
        Back.pack(in_=bottom, side=tk.RIGHT)

    def confirm(self):
        global QA7
        global A7
        if self.Q[0] == "C":
            self.answer = rQG.comboAns(self.Q[1], self.Q[2])
        elif self.Q[0] == "P":
            self.answer = rQG.permAns(self.Q[1], self.Q[2])
        A7 = self.answer
        QA7 = self.intVar.get()
        print(QA7)
        print(A7)
        self.controller.show_frame("Q8")


    def Quest(self):
        if self.Q[0] == "C":
            self.strVar.set("C(" + str(self.Q[1]) + ", " + str(self.Q[2]) + ") = :")
        elif self.Q[0] == "P":
            self.strVar.set("P(" + str(self.Q[1]) + ", " + str(self.Q[2]) + ") = :")
        else:
            self.strVar.set("ERROR!!")


class Q8(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Q = rQG.pickRandQuestion()
        self.QA = (self.Q[3:])
        self.QAS = shuffle(self.QA)
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.Quest()
        label.pack(side="top", fill="x", pady=10)
        self.intVar = tk.StringVar()
        self.intVar.set('python')
        R1 = tk.Radiobutton(self, text=str(self.QA[0]), variable=self.intVar, value=str(self.QA[0]))
        R1.pack(anchor=tk.W)
        R2 = tk.Radiobutton(self, text=str(self.QA[1]), variable=self.intVar, value=str(self.QA[1]))
        R2.pack(anchor=tk.W)
        R3 = tk.Radiobutton(self, text=str(self.QA[2]), variable=self.intVar, value=str(self.QA[2]))
        R3.pack(anchor=tk.W)
        R4 = tk.Radiobutton(self, text=str(self.QA[3]), variable=self.intVar, value=str(self.QA[3]))
        R4.pack(anchor=tk.W)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Back = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame("Q7"))
        Next = tk.Button(self, text="Next", command=self.confirm)
        Next.pack(in_=bottom, side=tk.RIGHT)
        Back.pack(in_=bottom, side=tk.RIGHT)

    def confirm(self):
        global QA8
        global A8
        if self.Q[0] == "C":
            self.answer = rQG.comboAns(self.Q[1], self.Q[2])
        elif self.Q[0] == "P":
            self.answer = rQG.permAns(self.Q[1], self.Q[2])
        A8 = self.answer
        QA8 = self.intVar.get()
        print(QA8)
        print(A8)
        self.controller.show_frame("Q9")


    def Quest(self):
        if self.Q[0] == "C":
            self.strVar.set("C(" + str(self.Q[1]) + ", " + str(self.Q[2]) + ") = :")
        elif self.Q[0] == "P":
            self.strVar.set("P(" + str(self.Q[1]) + ", " + str(self.Q[2]) + ") = :")
        else:
            self.strVar.set("ERROR!!")


class Q9(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Q = rQG.pickRandQuestion()
        self.QA = (self.Q[3:])
        self.QAS = shuffle(self.QA)
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.Quest()
        label.pack(side="top", fill="x", pady=10)
        self.intVar = tk.StringVar()
        self.intVar.set('python')
        R1 = tk.Radiobutton(self, text=str(self.QA[0]), variable=self.intVar, value=str(self.QA[0]))
        R1.pack(anchor=tk.W)
        R2 = tk.Radiobutton(self, text=str(self.QA[1]), variable=self.intVar, value=str(self.QA[1]))
        R2.pack(anchor=tk.W)
        R3 = tk.Radiobutton(self, text=str(self.QA[2]), variable=self.intVar, value=str(self.QA[2]))
        R3.pack(anchor=tk.W)
        R4 = tk.Radiobutton(self, text=str(self.QA[3]), variable=self.intVar, value=str(self.QA[3]))
        R4.pack(anchor=tk.W)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Back = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame("Q8"))
        Next = tk.Button(self, text="Next", command=self.confirm)
        Next.pack(in_=bottom, side=tk.RIGHT)
        Back.pack(in_=bottom, side=tk.RIGHT)

    def confirm(self):
        global QA9
        global A9
        if self.Q[0] == "C":
            self.answer = rQG.comboAns(self.Q[1], self.Q[2])
        elif self.Q[0] == "P":
            self.answer = rQG.permAns(self.Q[1], self.Q[2])
        A9 = self.answer
        QA9 = self.intVar.get()
        print(QA9)
        print(A9)
        self.controller.show_frame("Q10")

    def Quest(self):
        if self.Q[0] == "C":
            self.strVar.set("C(" + str(self.Q[1]) + ", " + str(self.Q[2]) + ") = :")
        elif self.Q[0] == "P":
            self.strVar.set("P(" + str(self.Q[1]) + ", " + str(self.Q[2]) + ") = :")
        else:
            self.strVar.set("ERROR!!")


class Q10(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Q = rQG.pickRandQuestion()
        self.QA = (self.Q[3:])
        self.QAS = shuffle(self.QA)
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.Quest()
        label.pack(side="top", fill="x", pady=10)
        self.intVar = tk.StringVar()
        self.intVar.set('python')
        R1 = tk.Radiobutton(self, text=str(self.QA[0]), variable=self.intVar, value=str(self.QA[0]))
        R1.pack(anchor=tk.W)
        R2 = tk.Radiobutton(self, text=str(self.QA[1]), variable=self.intVar, value=str(self.QA[1]))
        R2.pack(anchor=tk.W)
        R3 = tk.Radiobutton(self, text=str(self.QA[2]), variable=self.intVar, value=str(self.QA[2]))
        R3.pack(anchor=tk.W)
        R4 = tk.Radiobutton(self, text=str(self.QA[3]), variable=self.intVar, value=str(self.QA[3]))
        R4.pack(anchor=tk.W)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Back = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame("Q9"))
        Submit = tk.Button(self, text="Confirm", command=self.confirm)
        Submit.pack(in_=bottom,side=tk.RIGHT)
        Back.pack(in_=bottom, side=tk.RIGHT)


    def confirm(self):
        global QA10
        global A10
        if self.Q[0] == "C":
            self.answer = rQG.comboAns(self.Q[1], self.Q[2])
        elif self.Q[0] == "P":
            self.answer = rQG.permAns(self.Q[1], self.Q[2])
        A10 = self.answer
        QA10 = self.intVar.get()
        print(QA10)
        print(A10)
        self.controller.show_frame("Submit")


    def Quest(self):
        if self.Q[0] == "C":
            self.strVar.set("C(" + str(self.Q[1]) + ", " + str(self.Q[2]) + ") = :")
        elif self.Q[0] == "P":
            self.strVar.set("P(" + str(self.Q[1]) + ", " + str(self.Q[2]) + ") = :")
        else:
            self.strVar.set("ERROR!!")

class Submit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.strVar = tk.StringVar()
        self.label = tk.Label(self)
        test = tk.Button(self, text="Check", command=self.result)
        test.pack()
        self.label.pack()

    def result(self):
        global lessonName
        global cur
        global conn
        global i
        global User
        if QA1 == A1:
            print("correct")
            i+=1
        else:
            print("incorrect")
        if QA2 == A2:
            print("correct")
            i += 1
        else:
            print("incorrect")
        if QA3 == A3:
            print("correct")
            i += 1
        else:
            print("incorrect")
        if QA4 == A4:
            print("correct")
            i += 1
        else:
            print("incorrect")
        if QA5 == A5:
            print("correct")
            i += 1
        else:
            print("incorrect")
        if QA6 == A6:
            print("correct")
            i += 1
        else:
            print("incorrect")
        if QA7 == A7:
            print("correct")
            i += 1
        else:
            print("incorrect")
        if QA8 == A8:
            print("correct")
            i += 1
        else:
            print("incorrect")
        if QA9 == A9:
            print("correct")
            i += 1
        else:
            print("incorrect")
        if QA10 == A10:
            print("correct")
            i += 1
        else:
            print("incorrect")
        answertext = "You got " + str(i) + " correct"
        self.label.config(text=answertext)
        cur.execute("INSERT INTO TestScores(ID, TestID, Score) VALUES (%s, %s, %s)", (User, lessonName, int(i)))
        conn.commit()



if __name__ == "__main__":
    app = testApp()
    app.mainloop()