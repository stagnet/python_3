Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> 'PS4 | 350$ | BRAND NEW'
'PS4 | 350$ | BRAND NEW'
>>> 'PS4 | 350$ | BRAND NEW'
'PS4 | 350$ | BRAND NEW'
>>> data ='PS4 | 350$ | BRAND NEW'
>>> data
'PS4 | 350$ | BRAND NEW'
>>> product = data.index('|')
>>> product
4
>>> data[:4]
'PS4 '
>>> data.find('|') # to find out elemnts b/w '|' to next '|' we use find().......
4
>>> data.find('|', 5)
11
>>> data.find("|" , 10) # here in argument "|" means we want to find out '|' . and 10 means it is the start position from where the string slicing will start.........
11
>>> data[data.find('|')+1 : data.find('|' , 11)]
' 350$ '
>>> data.find('|' , 12)
-1
>>> data[11 : -1]
'| BRAND NE'
>>> data[12 : ]
' BRAND NEW'
>>> 
