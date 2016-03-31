import randomQuestionGenerator as rQG
from tkinter import *
from random import shuffle




# print(Q1A)
# if Q1[0] == "C":
#     print("C(" + str(Q1[1]) + ", " + str(Q1[2]) + ") = :")
#     for i in Q1A:
#         print (i)
#
# elif Q1[0] == "P":
#     print("P(" + str(Q1[1]) + ", " + str(Q1[2]) + ") = :")
#     for i in Q1A:
#         print(i)



class test(object):
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

        submit = Button(self.frame, text="Submit", command=self.sel)
        submit.pack()

        self.labelOpt = Label(self.frame)
        self.labelOpt.pack()
        reset = Button(self.frame, text = "Reset", command = self.res)
        reset.pack()


    def sel(self):
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

    def res(self):
        self.frame.destroy()
        test().main()


root = Tk()

root.title("Counting Test")

test().main()



root.mainloop()
