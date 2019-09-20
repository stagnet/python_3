file_1 = open("fruits.txt")
content = file_1.read()
file_1.close()
content = content.splitlines()
for i in content:
    print(len(i))