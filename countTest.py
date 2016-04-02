import randomCountingQuestionGenerator as rQG
import countQuestGet as QG
from tkinter import *
from random import shuffle



class randomQuest(object):
    def main(self):
        self.frame = Frame(root)
        self.frame.pack()
        self.Q1 = rQG.pickRandQuestion()
        self.Q1A = (self.Q1[3:])
        self.Q1AS = shuffle(self.Q1A)
        self.strVar = StringVar()
        labelStr = Label(self.frame, textvariable=self.strVar, relief=RAISED)
        self.Quest1()
        labelStr.pack()

        self.intVar = IntVar()
        R1 = Radiobutton(self.frame, text=str(self.Q1A[0]), variable=self.intVar, value=self.Q1A[0])
        R1.pack(anchor=W)
        R2 = Radiobutton(self.frame, text=str(self.Q1A[1]), variable=self.intVar, value=self.Q1A[1])
        R2.pack(anchor=W)
        R3 = Radiobutton(self.frame, text=str(self.Q1A[2]), variable=self.intVar, value=self.Q1A[2])
        R3.pack(anchor=W)
        R4 = Radiobutton(self.frame, text=str(self.Q1A[3]), variable=self.intVar, value=self.Q1A[3])
        R4.pack(anchor=W)

        submit = Button(self.frame, text="Submit", command=self.selr)
        submit.pack()

        self.labelOpt = Label(self.frame)
        self.labelOpt.pack()



    def selr(self):
        if self.Q1[0] == "C":
            answer = rQG.comboAns(self.Q1[1], self.Q1[2])
        elif self.Q1[0] == "P":
            answer = rQG.permAns(self.Q1[1], self.Q1[2])
        else:
            self.strVar.set("ERROR!!")
        if answer == self.intVar.get():
            answerText = "You are correct"
        else:
            answerText = "You are Wrong"
        self.labelOpt.config(text=answerText)

    def Quest1(self):
        if self.Q1[0] == "C":
            self.strVar.set("C(" + str(self.Q1[1]) + ", " + str(self.Q1[2]) + ") = :")
        elif self.Q1[0] == "P":
            self.strVar.set("P(" + str(self.Q1[1]) + ", " + str(self.Q1[2]) + ") = :")
        else:
            self.strVar.set("ERROR!!")

class Quest(object):
    def main(self, number):
        self.number = number
        self.frame = Frame(root)
        self.frame.pack()
        self.Q1 = QG.getQuestion(number)
        self.Q1A = QG.getAnswersShuffled(number)
        self.strVar = StringVar()
        labelStr = Label(self.frame, textvariable=self.strVar, relief=RAISED)
        self.strVar.set(QG.getQuestion(number))
        labelStr.pack()

        self.intVar = StringVar()
        R1 = Radiobutton(self.frame, text=str(self.Q1A[0]), variable=self.intVar, value=str(self.Q1A[0]))
        R1.pack(anchor=W)
        R2 = Radiobutton(self.frame, text=str(self.Q1A[1]), variable=self.intVar, value=str(self.Q1A[1]))
        R2.pack(anchor=W)
        R3 = Radiobutton(self.frame, text=str(self.Q1A[2]), variable=self.intVar, value=str(self.Q1A[2]))
        R3.pack(anchor=W)
        R4 = Radiobutton(self.frame, text=str(self.Q1A[3]), variable=self.intVar, value=str(self.Q1A[3]))
        R4.pack(anchor=W)

        submit = Button(self.frame, text="Submit", command=self.selr)
        submit.pack()

        self.labelOpt = Label(self.frame)
        self.labelOpt.pack()



    def selr(self):
        answer = QG.getCorrectAnswer(self.number)
        if answer == self.intVar.get():
            answerText = "You are correct"
        else:
            answerText = "You are Wrong"
        self.labelOpt.config(text=answerText)


def data():
    Quest().main(1)
    Quest().main(2)
    Quest().main(3)
    Quest().main(4)
    Quest().main(5)
    randomQuest().main()
    randomQuest().main()
    randomQuest().main()
    randomQuest().main()
    randomQuest().main()


root = Tk()
root.title("Counting Test")



data()


root.mainloop()
