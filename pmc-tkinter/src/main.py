from tkinter import *

window = Tk()

btn1 = Button(window, text="Execute")
btn1.grid(row=0, column=0)

entry1 = Entry(window)
entry1.grid(row=0, column=1)

text1 = Text(window, height=1, width=20)
text1.grid(row=0, column=2)

window.mainloop()
