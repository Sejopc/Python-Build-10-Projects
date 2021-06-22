from tkinter import *

# In Tkinter, we have a Window and Widget.

window=Tk()

# We create Widgets here.
b1 = Button(window, text="Execute") 
              # We have see which parameters this accepts by opnening a interactive python console (# ipython3) importing all Tkinter clases and methods (from tkinter import *) and
              # simply running: Button? - it will display the parameters it accepts. In this case, it needs the Tkinter window it will attach into (window variable from above) and
              # the button's text.
#b1.pack()
b1.grid(row=0,column=0) # We have more control on the position of our buttons and widgets than using "pack()"

e1 = Entry(window) # Text field entry. Similar as <input> in HTML. 
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20) # Text widget.
t1.grid(row=0, column=2)

window.mainloop() # This should be always at the end of your code.