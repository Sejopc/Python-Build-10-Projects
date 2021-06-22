from tkinter import *
from tkinter.messagebox import showinfo
# This will connect with the backend (database.py) database.

from backend_OOP import Database # Importing the Database class from backend script

database = Database("books.db")

def get_selected_row(event): # Takes the event parameter, which hold the information about the type of the event.
                             # In this case, the event it is receiving is <<ListboxSelect>>
    try:
        global selected_tuple

        index = list1.curselection()[0] # Gets the index of the selected row of the Listbox
        selected_tuple = list1.get(index) # This will grab the contents of the selected row (id,title,author,year,isbn)
    
        # Whenever the user selects a result (row) from the Listbox, we want to
        # populate the Entries with the values from the selected row.
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1]) # Title

        e2.delete(0,END)
        e2.insert(END, selected_tuple[2]) # Author

        e3.delete(0,END)
        e3.insert(END, selected_tuple[3]) # Year

        e4.delete(0,END)
        e4.insert(END, selected_tuple[4]) # ISBN
    except IndexError: # Empty ListBox
        pass

def view_all():
    list1.delete(0,END) # delete everything from row index 0 till the last row.
    for row in database.view():
        list1.insert(END, row) # END ensures every new row is inserted at the end of the listbox, so we don't have to manually specify the index.

def search_entry():
    list1.delete(0,END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_entry():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    showinfo("Window", "Entry added successfully.")

def delete_entry():
    database.delete(selected_tuple[0]) # Gets the ID of the selected row.
    view_all()

def update_entry():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_all()

window = Tk()

window.wm_title("Book Store")

l1 =  Label(window, text="Title")
l1.grid(row=0, column=0)

l1 =  Label(window, text="Author")
l1.grid(row=0, column=2)

l1 =  Label(window, text="Year")
l1.grid(row=1, column=0)

l1 =  Label(window, text="ISBN")
l1.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=7, columnspan=2) # Delete the "rowspan and columnsap arguments to understand what they do"

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=7)

# Attach List and Scrollbar to work together
list1.configure(yscrollcommand=scrollbar.set) # Vertical scrollbar along Y axis will be set to this scrollbar
scrollbar.configure(command=list1.yview) # Remember when we pass a "command" argument it will execute something upon interacting with the button/list/scrollbar etc. In this case
                                         # when we scroll the bar, the vertical view of the list will change.

list1.bind('<<ListboxSelect>>', get_selected_row)
# Bind method is used to bind a function to a widget event. 
# i.e we are binding a method to the Listbox (list1) Widget
# Takes 2 arguments: EventType (format: <<EventType>>), and the function to be bind.

b1 = Button(window, text="View all", width=12, command=view_all)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_entry)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_entry)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_entry)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_entry)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()