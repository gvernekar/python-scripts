# read line by line 

fobj = open ("languages.txt","r")

for line in fobj: 
    print (line)
    
fobj.close()





fobj = open ("languages.txt","r")

for line in fobj: 
    #remove whitespace at the end of each line
    line = line.strip()
    ## split the line with , as the delimeter
    data = line.split(",")
    # display 1st field
    print (data[0])
    
fobj.close()
