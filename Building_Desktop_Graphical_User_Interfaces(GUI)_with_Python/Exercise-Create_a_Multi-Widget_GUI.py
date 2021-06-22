from tkinter import *

window = Tk()

def convert_kg():
    # Empty the boxes if they had previous text.
    t1.delete("1.0", END)
    t2.delete("1.0", END)
    t3.delete("1.0", END)

    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274

    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)

# Label "Kg"
l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

# Create a special StringVar() Object
e1_value = StringVar() 

# Create an Entry box for users to input values
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# Create a button widget. Function "convert_kg" is called with button is pressed.
b1 = Button(window, text="Convert", command=convert_kg)  
b1.grid(row=0, column=2)

# Create three empty text boxes, t1, t2, t3
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

# This makes sure to keep the window open.
window.mainloop()