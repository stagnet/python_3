3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #MORE operations in dictionaries
>>> person ={'name':'ravi' ,"surname":'kumar' ,'age':'28'}
>>> person
{'name': 'ravi', 'surname': 'kumar', 'age': '28'}

>>> #removing pair....
>>> person.pop("name")
'ravi'
>>> person
{'surname': 'kumar', 'age': '28'}

>>> #Adding new pair...
>>> person["job"]="IT pro"
>>> person
{'surname': 'kumar', 'age': '28', 'job': 'IT pro'}

>>> #changing an existing value...
>>> person["age"]=30
>>> person
{'surname': 'kumar', 'age': 30, 'job': 'IT pro'}

>>> #MAPPING two lists to a dictionary:
>>> keys = ['a','b','c']
>>> values = [10,11,12]
>>> mydict = dict(zip(keys,values))
>>> mydict
{'a': 10, 'b': 11, 'c': 12}
>>> #......fin.....
