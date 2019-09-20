============================== RESTART: Shell ===============================
>>> race = 'race_is_always_against_time'.split('_')
>>> race
['race', 'is', 'always', 'against', 'time']
>>> race[2]
'always'
>>> race[0]
'race'
>>> race[:]
['race', 'is', 'always', 'against', 'time']
>>> race[:5]
['race', 'is', 'always', 'against', 'time']
>>> race[:2]
['race', 'is']
>>> race[-2]
'against'
>>> #[start : stop : step] we can use in lists slicing to..!!!
>>> race[:-1:2]
['race', 'always']
>>> race[:-1:-1]
[]
>>> race[:-1:1]
['race', 'is', 'always', 'against']

>>> race[:-1:3]
['race', 'against']
>>> race[:-1:4]
['race']
>>> race[:]
['race', 'is', 'always', 'against', 'time']
>>> 
>>> data = 'xbox0n3 / 250$'
>>> data
'xbox0n3 / 250$'
>>> data[0: :-1]
'x'
>>> data[0:4]
'xbox'
>>> data[0:-1]
'xbox0n3 / 250'
>>> data[:]
'xbox0n3 / 250$'
>>> data[: :-1]
'$052 / 3n0xobx'
>>> data[: :]
'xbox0n3 / 250$'
>>> data[0:14]
'xbox0n3 / 250$'
>>> data[0:14:-1]
''
>>> data[: :-1]
'$052 / 3n0xobx'
>>> 
>>> 
>>> race
['race', 'is', 'always', 'against', 'time']
>>> race[: : -1]
['time', 'against', 'always', 'is', 'race']
>>> 
=============================== RESTART: Shell ===============================

>>> data = 'xbox0n3 / 250$'
>>> data
'xbox0n3 / 250$'
>>> data.split('/')
['xbox0n3 ', ' 250$']
>>> detail = data.split('/')
>>> product= detail[0]
>>> product
'xbox0n3 '
>>> price = detail[1]
>>> price
' 250$'
>>> 
