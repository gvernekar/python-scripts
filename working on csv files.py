fobj = open("C:\\Users\\gvernekar\\Downloads\\Python_Examples\\datasets\\employees.csv")

for line  in fobj:
    line = line.strip()
    print (line)
    
fobj.close()



fobj = open("C:\\Users\\gvernekar\\Downloads\\Python_Examples\\datasets\\employees.csv")

for Gender  in fobj:
    Gender = Gender.strip()
    if "Female" in Gender:
        print (Gender)
    
fobj.close()




fobj = open("C:\\Users\\gvernekar\\Downloads\\Python_Examples\\datasets\\employees.csv","r")
malecount = 0
femalecount = 0
for line in fobj:
    array = line.split(',')
    if(array[1] == "Female"):
        femalecount = femalecount + 1
    if (array[1] == "Male"):
        malecount = malecount + 1 
        
        print(femalecount)
        