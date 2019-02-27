

# function body 
def add(first,second,third=0):
	total = first + second + third
	return total
print("Program begins from here")
gettotal = add(10,20)
print("Sum of the numbers :",gettotal)


gettotal = add(10,20,50)
print("Sum of the numbers :",gettotal)

print("Program ends from here")