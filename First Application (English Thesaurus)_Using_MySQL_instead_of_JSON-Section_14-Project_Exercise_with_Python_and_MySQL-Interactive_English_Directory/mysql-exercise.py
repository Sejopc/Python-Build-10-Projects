import mysql.connector

conn = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = conn.cursor()

word = input("Enter a word: ")

#query = cursor.execute("SELECT * FROM Dictionary") # will return ALL results
#query = cursor.execute("SHOW COLUMNS FROM Dictionary") # will show all the columns (in this case, 2) used by Dictionary table
#query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'inlay'") # will return only 1 tuple inside the list
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word) # will return 4 tuples inside the list

results = cursor.fetchall()

#print(results) # is made up of a list, with Tuples inside.
#print(results[0]) # Will get only the first result (tuple) from the list.

if results:
    for result in results:
        #print(result) # will get every result (tuple) for a keyword
        print(result[1]) # will get only the definition of the keyword for every result (tuple)
else:
    print("No word found!")