import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def myword(dict_word):
    if dict_word in data:
        dict_value = data[dict_word]
        return dict_value
    elif len(get_close_matches(dict_word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no. -> " % get_close_matches(dict_word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(dict_word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter a dictionary word: ").lower()

output = myword(word)
if type(output) == list:
    [print(item) for item in output]
else:
    print(output)
