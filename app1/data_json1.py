import json
data = json.load(open("data.json",'r'))
     
def english_dictionary(word):

    word = word.lower()
    return data[word]
     
w =input("Enter the word to find its meaning:")
     
try:
    for words in english_dictionary(w):
        print(words)
except KeyError:
    print("Please check your word again")


