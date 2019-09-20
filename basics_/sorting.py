#reverse().....; used to reverse the whole list.
'''course = ['arts', 'english', 'maths', 'compsci','chemistry']
course.reverse()
print(course)'''

#sort().....accending order
'''course = ['arts', 'english', 'maths', 'compsci','chemistry']
num = [1,4,3,6,34,21,12]
num.sort()
course.sort()
print(course)
print(num)'''

#sort().....decending order
'''course = ['arts', 'english', 'maths', 'compsci','chemistry']
num1 = [1,12,4,34,6,21,3]
course.sort(reverse=True)
num1.sort(reverse=True)
print(course)
print(num1) '''

#if we wanted a sorted version of our list without altering the original.....WE USE SORTED()...[FUNCTION]
course = ['arts', 'english', 'maths', 'compsci','chemistry']
new_sorted= sorted(course)#sorted function doesn't sort the list  in place, it return a value sorted version of a list by creating a  new variable and set it to the return value pf the sorted.
print(new_sorted)

#min()function
num = [1,4,3,6,34,21,12]
print(min(num))

#max()function
num = [1,4,3,6,34,21,12]
print(max(num))

#sum()function
num = [1,4,3,6,34,21,12]
print(sum(num))
