import glob#import glob lib
from datetime import datetime

filenames = glob.glob("*.txt")# create a variable named filenames and save the files who have .txt...

with open(datetime.now().strftime("%Y-%m-%d-%H")+".txt" , "w") as file:#create a new file which names as the 
    #current time stamp with formatted and asign the value in the "file" variable..

    for filename in filenames:# start loop in which the value of all .txt files iterates 
        with open(filename , "r")as content:#creates a new variable "content" which is readable  
            # file that only read the values of iterables..
           file.write(content.read() + "\n")#uses write() to write the 