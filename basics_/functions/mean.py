temprature = [23,32,10]
student_grade = {'raj':9.2, 'john':8.3,'peter':10.2}

def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values())/ len(value)
    else:
        the_mean = sum(value)/ len(value)
    return the_mean
print(mean(student_grade))