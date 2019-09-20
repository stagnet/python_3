#concatination 01
greeting = 'hello'
name = 'micheal'
message = greeting + ', ' + name
print(message)

#concatination 02
greeting = 'hello'
name = 'micheal'
message = '{}, {}. welcome home!'.format(greeting,name)#these are called placeholders {}
print(message)

#advance string formating....[F string]

greeting = 'hello'
name = 'micheal'
message = f'{greeting.lower()}, {name.upper()}. welcome home!'
print(message)

#function call....
def call(name):
    return f'hi {name.upper()}'
print(call('abhi'))

# complex string formatting.....
user_name = input("Name please: ")
user_expreience = int(input("Experience in years: "))
print( f'Hi {user_name.title()}, you have {user_expreience} year of working experience')