from tkinter import *


def km_to_miles():
    # print(entry1_value.get())
    miles = float(entry1_value.get()) * 1.6
    text1.insert(END, str(miles))


window = Tk()

btn1 = Button(window, text="Execute", command=km_to_miles)
btn1.grid(row=0, column=0)

entry1_value = StringVar()

entry1 = Entry(window, textvariable=entry1_value)
entry1.grid(row=0, column=1)

text1 = Text(window, height=1, width=20)
text1.grid(row=0, column=2)

window.mainloop()
