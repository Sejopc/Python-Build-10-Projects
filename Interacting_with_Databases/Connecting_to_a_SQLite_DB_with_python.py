import sqlite3 # We dont need to install it, as it is built-in in python

"""
1. Connect to a DB
2. Create a cursor object
3. Write a SQL Query
4. Commit changes to DB
5. Close the connection to DB
"""

def create_table():
    conn = sqlite3.connect("lite.db") # We pass the DB File. If file doesn't exist, it will be created.

    cursor = conn.cursor()

    # cursor.execute("CREATE TABLE store (item TEXT, quantity INT, price REAL)") # REAL is a Float in python (decimal point number)
    # Above SQL query is meant to be run ONLY ONE time, and that is, the first time the program gets executed, as it will create a TABLE. If you run it again, it will give
    # error because TABLE already exist. HOWEVER, There is a way to avoid this, and is using "CREATE TABLE IF NOT EXISTS <table>", as so:
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INT, price REAL)")
    
    conn.commit() # Commit changes to SB
    conn.close()


def insert_data(item, quantity, price):
    conn = sqlite3.connect("lite.db") # We pass the DB File. If file doesn't exist, it will be created.
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    conn.commit() # Commit changes to SB
    conn.close()



def view():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall() 
    conn.close() # No need to use commit() method as we are not updating the Table, only selecting records.
    return rows

create_table()
insert_data("Water Glass", 10, 20.99)
insert_data("Coffee Cup", 5, 5.20)

print(view())