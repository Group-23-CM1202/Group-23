from tkinter import *
from tkinter import ttk
import os
import sys

def openLogic():	#closes current window and opens Logic lesson/test
	root.destroy()
	os.system("python logicTest.py")

def openCounting():	#closes current window and opens Counting lesson/test
	root.destroy()
	os.system("python countTestNew.py")

root = Tk()
root.title("Group 23")

mainframe = ttk.Frame(root, padding="3 5 1 1")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="").grid(column=1, row=2, columnspan=3, sticky=(W, E))	#spacer
ttk.Label(mainframe, text="").grid(column=2, row=3, sticky=(W, E))	#spacer
ttk.Label(mainframe, text="").grid(column=1, row=4, columnspan=3, sticky=(W, E))	#spacer

ttk.Label(mainframe, text="Group 23 Counting and Logic").grid(column=1, row=1, columnspan=3)
ttk.Label(mainframe, text="lesson and test").grid(column=1, row=2, columnspan=3)
ttk.Button(mainframe, text="Counting", command=openCounting).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Logic", command=openLogic).grid(column=3, row=3, sticky=E)

photo = PhotoImage(file="cardiffLogo.gif")
ttk.Label(mainframe, image=photo).grid(column=1, row=5, columnspan=3)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()