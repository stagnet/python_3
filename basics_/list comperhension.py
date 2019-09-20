temps = [221,345,224,556]
new_temps = [temp/10 for temp in temps]

print(new_temps)
    
#* list comperhension with if conditional..
temps = [223,434,533,313,-999]
new_temp = [temp/10 for temp in temps if temp != -999]#! here we want to remove the negetive data from the output

print(new_temp)

#* list comprehension with if-else...
raw_data = [23, 43, 56, -999, -234]
new_data = [data/10 if data > 0 else 0 for data in raw_data]#TODO this will replace every -ve no. with zero
print(new_data)

#* list comprehension inside method...
num = ['2.3', '4.3', '7.8', '77.3']

def convert_to_sum(num):
    return sum([float(i) for i in num])
