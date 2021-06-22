from tkinter import *

window=Tk()

def km_to_miles():
    t1.delete('1.0', END) # Clears the Widget every time we click on the "Execute" button.
    print(e1_value.get()) # Gets the string.
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles) # 1st arg: position where we want to insert the text.

b1 = Button(window, text="Execute", command=km_to_miles)  # Command parameters takes a function as an argument that will be called.

b1.grid(row=0,column=0) 

e1_value = StringVar()

e1 = Entry(window, textvariable=e1_value) # e1_value is the variable that will hold the value we enter in the Entry field.
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

# This makes sure to keep the window open.
window.mainloop()