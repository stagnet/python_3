numbers = [1,2,3,4]
file_1 = open("nubers.txt" , "w")# "w"  mode is used when we create a new file and write....
for i in numbers:
     file_1.write(str(i) + "\n")
file_1.close()