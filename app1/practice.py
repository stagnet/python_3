# COMPLETE WHOLE CODE USING MEMORY
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):

    w = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(w, data.keys(),cutoff =0.8))>0:
        yn = input(f'do you mean {get_close_matches(w, data.keys())[0]},Y for yes & N for no: ')
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "word does not exist"
        else:
            return "we don't understand your entry....."

    else:
        return("word doesn't exist")
w = input("enter the word: ")
output = translate(w)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
