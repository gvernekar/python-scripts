#write a program to read the file and replace the lines containing "Business 

#Development"  to "Information technology" and write the output to other file.

fobj = open("C:\\Users\\gvernekar\\Downloads\\Python_Examples\\datasets\\employees.csv", "r")
header = fobj.readline()

for line in fobj:
    line = line.strip()
    line = line.split(",")
    line = line.replace("Business Development","IT")
    fw.write(line + "\n")

fr.close()
fr.close()

