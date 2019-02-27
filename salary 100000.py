
fobj = open("C:\\Users\\gvernekar\\Downloads\\Python_Examples\\datasets\\employees.csv", "r")
for line in fobj:
    array = line.split(',')
    if(array[4] != "Salary"):
        if (int(array[4]) > 100000):
            print(line) 
fobj.close()