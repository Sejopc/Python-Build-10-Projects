import json
from difflib import get_close_matches
import mysql.connector

conn = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = conn.cursor()

word = input("Enter a dictionary word: ").lower()

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

def myword(possible_values):
    result_list = []
    cursor.reset()
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % possible_values)
    results = cursor.fetchall()
    for result in results:
        result_list.append(result[1])
    return result_list

if not results:
    try:
        cursor.reset()
        query = cursor.execute("SELECT * FROM Dictionary")
        results = cursor.fetchall()
        possible_values = get_close_matches(word, [key[0] for key in results], 1)[0]
        # I could've also just write: difflib.get_close_matches(word, data.keys())
        didyoumean = input('Did you mean: '+ possible_values + ' ? (Y, N): ')
        if didyoumean.lower() == 'y':
            didyoumean = possible_values
            for value in myword(didyoumean):
                print(value)
        else:
            print("Word not in dictionary.")
    except IndexError:
        print("Word doesn't exist.")
else:
    for result in results:
        print(result[1])
