#!/usr/bin/python

from tkinter import *

def onClick():
	pass


lesson = Tk()
lesson.geometry("1920x1080")
text = Text(lesson)
text.insert(INSERT, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam sollicitudin turpis ac quam sollicitudin, eget consectetur purus dignissim. Nulla at tempus arcu. Sed id lectus eu tellus ornare venenatis. Praesent congue nec mi vel aliquam. Cras cursus imperdiet mollis. Proin nec turpis risus. Ut et eros eu nunc congue mattis. Fusce odio quam, accumsan nec nibh ut, porta vehicula nisi. Fusce libero massa, elementum a nibh sed, consequat viverra nisl. Vestibulum gravida nibh hendrerit dolor congue, ut faucibus metus ornare. Ut pulvinar ac ipsum eget sagittis. Vivamus vel turpis dapibus lorem tempus vestibulum.")
text.pack()
def openTest():
	pass



B = Button(lesson, text = "Test!", command = openTest)
B.pack()
lesson.mainloop()