phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for keys, values in phone_numbers.items():
    print(keys + ': ' +values)



#Loop Over Dictionary and Replace (E)

#Loop over the phone_numbers values and in each loop print out the phone number, but with '00' instead of '+'. In other words, your code should output:
#0037682929928
#00423998200919
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for number in phone_numbers.values():
    print(number.replace('+','00'))
    