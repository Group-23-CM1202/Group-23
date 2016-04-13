import tkinter as tk
import randomCountingQuestionGenerator as rQG
import logicQuestGet as QG
import getLesson as GL
import dbTestresults as Test
from pymysql import connect, err, sys, cursors
from random import shuffle
from PIL import ImageTk, Image

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
        for F in (User, lessonPart1, lessonPart2, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Submit):
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

lesson = GL.getLessonContent(1)
questions = QG.whichQuest()
lessonName = str(GL.getLessonID(1))
Name = ''
User = ''
QA1 = ''
A1 = QG.getCorrectAnswer(questions[0])
QA2 = ''
A2 = QG.getCorrectAnswer(questions[1])
QA3 = ''
A3 = QG.getCorrectAnswer(questions[2])
QA4 = ''
A4 = QG.getCorrectAnswer(questions[3])
QA5 = ''
A5 = QG.getCorrectAnswer(questions[4])
QA6 = ''
A6 = QG.getCorrectAnswer(questions[5])
QA7 = ''
A7 = QG.getCorrectAnswer(questions[6])
QA8 = ''
A8 = QG.getCorrectAnswer(questions[7])
QA9 = ''
A9 = QG.getCorrectAnswer(questions[8])
QA10 = ''
A10 = QG.getCorrectAnswer(questions[9])

i = 0


class lessonPart1(tk.Frame):
    def __init__(self, parent, controller):
        global lesson
        tk.Frame.__init__(self, parent)
        self.controller = controller
        top = tk.Frame(self)
        top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        photo = tk.PhotoImage(file=lesson[0])
        panel = tk.Label(self, image = photo)
        panel.image = photo
        panel.pack(in_=top)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Next = tk.Button(self, text="Next",
                         command=lambda: controller.show_frame("lessonPart2"))
        Next.pack(in_=bottom, side=tk.RIGHT)



class lessonPart2(tk.Frame):
    def __init__(self, parent, controller):
        global lesson
        tk.Frame.__init__(self, parent)
        self.controller = controller
        top = tk.Frame(self)
        top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        photo = tk.PhotoImage(file=lesson[1])
        panel = tk.Label(self, image=photo)
        panel.image = photo
        panel.pack(in_=top)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        Next = tk.Button(self, text="Test",
                         command=lambda: controller.show_frame("Q1"))
        Next.pack(in_=bottom, side=tk.RIGHT)
        Back = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame("lessonPart1"))
        Back.pack(in_=bottom, side=tk.RIGHT)





class User(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        top = tk.Frame(self)
        top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        top2 = tk.Frame(self)
        top2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        L1 = tk.Label(self, text="Student ID")
        L1.pack(in_=top, side=tk.LEFT)
        self.username = tk.Entry(self, bd=5)
        self.username.pack(in_=top, side=tk.RIGHT)
        L2 = tk.Label(self, text="Name")
        L2.pack(in_=top2, side=tk.LEFT)
        self.Name = tk.Entry(self, bd=5)
        self.Name.pack(in_=top2, side=tk.RIGHT)
        bottom = tk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        submit = tk.Button(self, text='Submit', command=self.submit)
        submit.pack(in_=bottom, side=tk.RIGHT)
        self.label = tk.Label(self)
        self.label.pack(in_=bottom, side=tk.RIGHT)


    def submit(self):
        global Name
        global User
        ID = self.username.get()
        Name = self.Name.get()
        if len(ID) != 8:
            self.label.config(text="Invalid ID")
        elif (ID[1:]).isdigit() != True:
            self.label.config(text="Invalid ID")
        else:
            User = ID
            Name = Name
            self.controller.show_frame("lessonPart1")


class Q1(tk.Frame):
    def __init__(self, parent, controller):
        global questions
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.QA = QG.getAnswersShuffled(questions[0])
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(questions[0]))
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
        print(questions[0])

    def confirm(self):
        global QA1
        QA1 = self.intVar.get()
        print (QA1)
        self.controller.show_frame("Q2")




class Q2(tk.Frame):

    def __init__(self, parent, controller):
        global questions
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.QA = QG.getAnswersShuffled(questions[1])
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(questions[1]))
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
        print(questions[1])

    def confirm(self):
        global QA2
        QA2 = self.intVar.get()
        print(QA2)
        self.controller.show_frame("Q3")



class Q3(tk.Frame):

    def __init__(self, parent, controller):
        global questions
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.QA = QG.getAnswersShuffled(questions[2])
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(questions[2]))
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
        print(questions[2])

    def confirm(self):
        global QA3
        QA3 = self.intVar.get()
        print(QA3)
        self.controller.show_frame("Q4")



class Q4(tk.Frame):

    def __init__(self, parent, controller):
        global questions
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.QA = QG.getAnswersShuffled(questions[3])
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(questions[3]))
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
        print(questions[3])

    def confirm(self):
        global QA4
        QA4 = self.intVar.get()
        print(QA4)
        self.controller.show_frame("Q5")




class Q5(tk.Frame):

    def __init__(self, parent, controller):
        global questions
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.QA = QG.getAnswersShuffled(questions[4])
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(questions[4]))
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
        print(questions[4])

    def confirm(self):
        global QA5
        QA5 = self.intVar.get()
        print(QA5)
        self.controller.show_frame("Q6")




class Q6(tk.Frame):
    def __init__(self, parent, controller):
        global questions
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.QA = QG.getAnswersShuffled(questions[5])
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(questions[5]))
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
        print(questions[5])

    def confirm(self):
        global QA6
        QA6 = self.intVar.get()
        print(QA6)
        self.controller.show_frame("Q7")




class Q7(tk.Frame):

    def __init__(self, parent, controller):
        global questions
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.QA = QG.getAnswersShuffled(questions[6])
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(questions[6]))
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
        print(questions[6])

    def confirm(self):
        global QA7
        QA7 = self.intVar.get()
        print(QA7)
        self.controller.show_frame("Q8")


class Q8(tk.Frame):

    def __init__(self, parent, controller):
        global questions
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.QA = QG.getAnswersShuffled(questions[7])
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(questions[7]))
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
        print(questions[7])

    def confirm(self):
        global QA8
        QA8 = self.intVar.get()
        print(QA8)
        self.controller.show_frame("Q9")




class Q9(tk.Frame):

    def __init__(self, parent, controller):
        global questions
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.QA = QG.getAnswersShuffled(questions[8])
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(questions[8]))
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
        print(questions[8])

    def confirm(self):
        global QA9
        QA9 = self.intVar.get()
        print(QA9)
        self.controller.show_frame("Q10")




class Q10(tk.Frame):

    def __init__(self, parent, controller):
        global questions
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.QA = QG.getAnswersShuffled(questions[9])
        self.strVar = tk.StringVar()
        label = tk.Label(self, textvariable=self.strVar, relief=tk.RAISED)
        self.strVar.set(QG.getQuestion(questions[9]))
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
        Submit = tk.Button(self, text="Submit", command=self.confirm)
        Submit.pack(in_=bottom,side=tk.RIGHT)
        Back.pack(in_=bottom, side=tk.RIGHT)
        print(questions[9])


    def confirm(self):
        global QA10
        QA10 = self.intVar.get()
        print(QA10)
        self.controller.show_frame("Submit")


class Submit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.strVar = tk.StringVar()
        self.label = tk.Label(self)
        test = tk.Button(self, text="Confirm", command=self.result)
        test.pack()
        self.label.pack()


    def result(self):
        global i
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
        Test.insert(str(Name), str(User), int(lessonName), int(i))


if __name__ == "__main__":
    app = testApp()
    app.mainloop()