import sqlite3 # We dont need to install it, as it is built-in in python

"""
1. Connect to a DB
2. Create a cursor object
3. Write a SQL Query
4. Commit changes to DB
5. Close the connection to DB
"""

def create_table():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INT, price REAL)")

    conn.commit() 
    conn.close()


def insert_data(item, quantity, price):
    conn = sqlite3.connect("lite.db") 
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    conn.commit() 
    conn.close()



def view():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall() 
    conn.close()
    return rows

def delete_data(item):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item = ?",(item,))
    conn.commit()
    conn.close()

def update_data(quanity, price, item):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quanity, price, item))
    conn.commit()
    conn.close()

create_table()

delete_data('Wine Glass')
update_data(100, 30.99, 'Coffee Cup')

print(view())