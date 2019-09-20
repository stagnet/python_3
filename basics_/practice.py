'''x=1
y=2
z=3
pro_= (x*y)**z/8 ;
print(pro_)'''

#list slicig.....
letters = 'abcdefghijklnopqrstuvwxyz'
print(letters[-2])
print(letters[-3:-1])# SLICING IS UPPER exclusive bound
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(mylist[17])
# Append the last item of list1 to list2
list1 = [1.2323442655, 1.4534345567, 1.023458894]
list2 = [1.9934332091]
list2.append(list1[-1])
print(list2)

#please concatenate the first with the last item of mylist and store the output in a variable named c.make sure you list indexingself.
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c= mylist[0]+mylist[-1]
print(c)
#
