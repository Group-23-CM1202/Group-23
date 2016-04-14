from tkinter import *
from pymysql import connect, err, sys, cursors
import dbStudent as Student
from tkinter import messagebox as tm
import os
import sys

conn = connect("csmysql.cs.cf.ac.uk", user = 'c1455582', passwd = 'jzgwyT8pK', db = 'c1455582')
cur = conn.cursor()


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.logbtn = Button(self, text="Register", command=self._register_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        Username = self.entry_1.get()
        Password = self.entry_2.get()

        print(Username, Password)
        if any(Username in s for s in Student.getStudentID()):
            i = Student.getStudentID().index(Username)
            print(i)
            if Password == Student.getStudentPassword(i):
                tm.showinfo("info", "Login Successful")
                root.destroy()
                os.system("python Main.py")
            else:
                tm.showerror("info", "Login Failed")
        else:
            tm.showerror("info", "Login Failed")

    def _register_btn_clicked(self):
        ID = self.entry_1.get()
        Password = self.entry_2.get()
        if len(ID) != 8:
            tm.showinfo("info", "Invalid ID")
        elif (ID[1:]).isdigit() != True:
            tm.showinfo("info", "Invalid ID")
        else:
            Name = 'Test Name'
            Username = ID
            Password = Password
            Student.insert(str(Name), str(Username), str(Password))
            tm.showinfo("info", "Register Successful")

root = Tk()
lf = LoginFrame(root)
root.mainloop()