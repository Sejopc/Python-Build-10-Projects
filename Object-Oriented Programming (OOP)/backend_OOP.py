# Created for Lecture 206 - Coding the backend (Coding_the_backend.py)
import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn)) # first one is NULL because that's the ID, which is an autoincrement value, so we don't need to pass anything. 
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="",author="",year="",isbn=""): # user may pass only 1 parameters, so we need to put the others as empty
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    # This method is call when the program ends (i.e when the user clicks the "Close" button or simply presses the 'X')
    def __del__(self): # Special method for destructing the calling object.
                       # The __del__() method is a known as a destructor method 
                       # in Python. It is called when all references to the object 
                       # have been deleted i.e when an object is garbage collected.
        print("Database close.")
        self.conn.close()
        # https://www.geeksforgeeks.org/destructors-in-python/#:~:text=The%20__del__()%20method,an%20object%20is%20garbage%20collected.&text=Note%20%3A%20A%20reference%20to%20objects,or%20when%20the%20program%20ends.