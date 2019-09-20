#in this snippet the temprature variable is a list, which 
# iterates and call over the function cel_to_feh..
temprature = [10,-20,100]
def cel_to_feh(celsius):
    fahrenheit = celsius*9/5+32
    return fahrenheit

for tempratures in temprature:
    print(cel_to_feh(tempratures))