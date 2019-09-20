my_file = open("sample.txt" ,"a+")
content = my_file.read()# use new var so, system can read the data inside the sample.txt...
my_file.seek(0)

my_file.write("melon\npeach\n")#This line will appendnew lines in the existing txt file
    
my_file.close()
print(content)
