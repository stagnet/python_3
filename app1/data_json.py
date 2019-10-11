import json
from difflib import get_close_matches
dict = json.load(open("data.json"))

def meanings(word):#this function will used to call the word inside datasets..
    word= word.lower()#this will convert any word into a lower case...
    if word in dict: # here if word is in json file then,it will return the meaning of it..
        return dict[word]
    elif word.title() in dict:# title()..Return a version of the string where each word is titlecased.
               #More specifically, words start with uppercased characters and all remaining cased characters have lower case.
        return dict[word.title()]
    elif word.upper() in dict:
        return dict[word.upper()]

    elif len(get_close_matches(word,dict.keys(),cutoff = 0.8))>0:#elif statement will give user the suggested right word if he writes the wrong or misspelled word...
            yn = input(f'do you mean {get_close_matches(word,dict.keys(),cutoff = 0.8)[0]}, Y for yes or N for no :')
            if yn == "Y":
                return dict[get_close_matches(word,dict.keys(),cutoff = 0.8)[0]]
            elif yn == 'N':
                return "the word doesn't exist, Please double check it"
            else:
                return "we didn't understand your entry"
                
    else:
        return("this word does not exist in dictionary:")
w = input("enter the word :")# here user will enter the word...
#HERE WE WANT A NEW FEATURE THAT WILL HELP TO GIVE USER A GOOD LOOKING MEANINGS RATHER THAN THE LIST FORMAT

output = meanings(w)# Here we create a new varible "output" that will assign the value of fuction call
if type(output) == list:#Here we build a logic to run the loop if the type of the output is list format...
        for item in output:#then loop will run and  prints all possible meanings of a single word in a structured form...
                print(item)
else:
        print(output)
        
