import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean '%s' instead? Enter Y for yes, N for no: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word you entered doesn't exist."
        else:
            return "We didn't understand your input."
    else:
        return "The word doesn't exist, please correct it."

word = input("Enter your word: ")
output = (translate(word))

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
