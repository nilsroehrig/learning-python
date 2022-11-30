from tkinter import *


def calculate():
    kilograms = float(var_kilograms.get())
    var_grams.set(str(kilograms * 1000))
    var_pounds.set(str(kilograms * 2.20462))
    var_ounces.set(str(kilograms * 35.274))


window = Tk()

lbl_kilograms = Label(window, text="Kilograms")
var_kilograms = StringVar()
ent_kilograms = Entry(window, textvariable=var_kilograms, width=50)

btn_convert = Button(window, text="Convert", width=25, command=calculate)

lbl_grams = Label(window, text="Grams")
var_grams = StringVar()
txt_grams = Entry(window, textvariable=var_grams, width=20, state="disabled")

lbl_pounds = Label(window, text="Pounds")
var_pounds = StringVar()
txt_pounds = Entry(window, textvariable=var_pounds, width=20, state="disabled")

lbl_ounces = Label(window, text="Ounces")
var_ounces = StringVar()
txt_ounces = Entry(window, textvariable=var_ounces, width=20, state="disabled")

lbl_kilograms.grid(row=0, column=0, padx=5, pady=5, sticky="w")
ent_kilograms.grid(row=0, column=1, columnspan=4, padx=5, pady=5, sticky="w")
btn_convert.grid(row=0, column=4, columnspan=2, padx=5, pady=5, sticky="w")

lbl_grams.grid(row=1, column=0, padx=5, pady=5, sticky="w")
txt_grams.grid(row=1, column=1, padx=5, pady=5, sticky="w")

lbl_pounds.grid(row=1, column=2, padx=5, pady=5, sticky="w")
txt_pounds.grid(row=1, column=3, padx=5, pady=5, sticky="w")

lbl_ounces.grid(row=1, column=4, padx=5, pady=5, sticky="w")
txt_ounces.grid(row=1, column=5, padx=5, pady=5, sticky="w")

window.mainloop()
