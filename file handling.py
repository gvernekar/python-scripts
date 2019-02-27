fobj = open ("demo.txt", "w")

fobj.write ("python programming\n")
fobj.write ("ruby programming\n")
fobj.write ("scala programming\n")

fobj.close()



name = input("enter text : ")

fobj = open ("demo1.txt", "a") 

fobj.write (name)

fobj.close()
