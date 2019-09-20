my_files = open("sample.txt")
content_inside_my_file = my_files.read()
my_files.close()# Be in habit of using close(), as it release the memory after the file is read...
print(content_inside_my_file) 