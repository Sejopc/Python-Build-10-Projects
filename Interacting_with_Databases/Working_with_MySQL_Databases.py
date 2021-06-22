# In previous videos, I explained how to interact with PostGreSQL databases. If you prefer to work with MySQL instead of PostGreSQL, see the code further down.

# I set up a remote MySQL database on a server with the IP address 108.167.140.122, so you don't have to install and set up a MySQL database yourself. To connect and query data from that remote database, you need a username, password, and the name of the database. These are written inside the Python script below.

# You also need a Python library that interacts with MySQL databases. Many libraries are compatible, but I prefer mysql.connector. To install mysql.connector: simply execute pip install mysql-connector  or pip3 install mysql-connector depending on whether you use pip or pip3. Once you install the library, try this working example:

import mysql.connector

word = input("Enter a word in English and press Enter: ")
con = mysql.connector.connect(
    user="ardit700_student", 
    password = "ardit700_student", 
    host="108.167.140.122", 
    database = "ardit700_pm1database"
)
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
if results:
    for result in results:
        print(result[1])
else:
    print("We couldn't find any results about that.")