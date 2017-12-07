# Instructions
#
# There's currently a bug in the program app86.py. When the user inputs a proper noun (e.g. Delhi, Paris, etc.)
# the program will convert it to lowercase and then tries to find the lowercase version (e.g. delhi) in the dataset and
# it cannot find it since the dataset has Delhi, but not delhi.

# Please add another conditional block to the program so that the program returns the definition
# of names that start with a capital letter. You can find the code we have so far attached here in
# this lecture for your convenience.


import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)