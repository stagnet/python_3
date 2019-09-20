'''ADD SOME VALUES IN LIST'''
#append()...TO ADD SOMETHING IN THE END OF LIST
course = ['arts', 'english', 'maths', 'compsci','chemistry']
course.append('boilogy'.upper());
print(course)

#insert()....;TO ADD SOMETHING TO A SPECIFIC LOCATION OUR LIST
course = ['arts', 'english', 'maths', 'compsci','chemistry']
course_2 = ['ARMADA']
course.insert(2,course_2)# uses two arguments index values & value itself respectivly....
print(course)

 #extend().....;IT IS USE WHEN WE WANT TO ADD VALUES OF ANOTHER LIST IN THE ORIGINAL ONE AND VICE-VERSE
course = ['arts','english','maths','compsci','chemistry']
course_2 = ['Biology','education']
course.extend(course_2)
print(course)

'''REMOVE SOME VALUES IN list'''
#remove()...
course = ['arts', 'english', 'maths', 'compsci','chemistry']
course.remove('arts')
print(course)

#pop()...
course = ['arts', 'english', 'maths', 'compsci','chemistry']
popped= course.pop(1)# so,pop() can return the value that it removed. so we can set a value and grab that value and return them...
print(popped)
print(course)
