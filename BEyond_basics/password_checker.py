correct_password = "pythonic123"
name = input("enter your name: ")
user_password = input("enter the password: ")

while correct_password != user_password:
    user_password = input("wrong ! try again: ")
    
print(f"{name.upper()}, how you are doing:")	
