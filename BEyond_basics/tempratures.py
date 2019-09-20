#One solution is to open a file once and then iterate inside the function while the file is open:
temprature = [10, -20, -289, 100]
def values(temprature):
        with open("tempratures.txt", "w") as my_files:
                for c in temprature:
                        if c> -273.15:
                                f= c*9/5+32
                                my_files.write(str(f) + "\n")
values(temprature)
# This program is creating a new txt file and then converts the values in the list into farenhite and then prints them in the txt file....