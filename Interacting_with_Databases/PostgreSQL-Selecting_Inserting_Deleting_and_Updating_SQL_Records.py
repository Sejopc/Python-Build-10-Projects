import psycopg2 

def create_table():
    conn = psycopg2.connect(" dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INT, price REAL)")
    conn.commit() 
    conn.close()


def insert_data(item, quantity, price):
    conn = psycopg2.connect(" dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")
    cursor = conn.cursor()
    # cursor.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, quantity, price))  # PRONE TO SQL Injections! Not secure.  
    cursor.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price)) # MORE SECURITY SAFE
    conn.commit() 
    conn.close()

def view():
    conn = psycopg2.connect(" dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall() 
    conn.close()
    return rows

def delete_data(item):
    conn = psycopg2.connect(" dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item = %s",(item,))
    conn.commit()
    conn.close()

def update_data(quanity, price, item):
    conn = psycopg2.connect(" dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quanity, price, item))
    conn.commit()
    conn.close()

create_table()

# Once this script is executed, go to pgAdmin4, to database1 > Schemas > public > Tables, and we will see the store Table with its columns and information.

#insert_data("Orange", 10, 15)
# After inserting data, go to pgAdmin4, click on your dabatase1, and then on the "Query tool" button to run the following:
# SELECT * FROM store 
# And you will see the inserted data there.

#delete_data('Wine Glass')
#update_data(100, 30.99, 'Coffee Cup')

#delete_data('Orange')
update_data(100, 20.55, 'Apple')
print(view())
