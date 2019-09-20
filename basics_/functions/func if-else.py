mystring = input("enter the value")
def string_length(mystring):
    if type(mystring)== int:
        return "sorry,integers don't have length"
    elif type(mystring)== float:
        print("sorry float don't have length either")
    else:
        return len(mystring)
print(string_length(mystring))