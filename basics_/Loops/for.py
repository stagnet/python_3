'''i=0#prints table of 2.....
while i<20:
    i=i+2
    print(i)
for i in range(20):#prints 0to19.....

    print(i)'''
    #for loop practice...
'''my_list = [1,2,3,4,5,6,7]
for i in my_list:
    print(i)'''

a = "Tricky"
for i in a[:3]:
    print(i)

mylist = ["Terribly Tricky"]
for word in mylist:
    for letter in word[-6:]:
        print(letter)

#for loop with conditional block
my_list =[1,2,3,4,5,6]
for i in my_list:
    if i>2:
        print(i)