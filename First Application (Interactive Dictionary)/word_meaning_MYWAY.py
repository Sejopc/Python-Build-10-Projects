import json
import difflib

data = json.load(open("data.json"))
word = input("Enter a dictionary word: ").lower()

def myword(dict_word):
    #if dict_word in data: <- IS REDUNDANT, because we are already checking for it.
    dict_value = data[dict_word]
    return ''+'\n'.join(dict_value)
    #else:
    #    return "The word doesn't exist. Please double check it."

if word not in data:
    try:
        possible_values = difflib.get_close_matches(word, [key for key in data], 1)[0]
    # I could've also just write: difflib.get_close_matches(word, data.keys())
        didyoumean = input('Did you mean: '+ possible_values + ' ? (Y, N): ')
        if didyoumean.lower() == 'y':
            didyoumean = possible_values
            print(myword(didyoumean))
        else:
            print("Word not in dictionary.")
    except IndexError:
        print("Word doesn't exist.")
else:
    print(myword(word))
