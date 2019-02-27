## list methods 

alist = [10,20,30,40]

alist.append(50)

print("after appending:", alist)


#alist.clear()
#print(alist)


alist.extend([60,70,80,10,10])

print ("after extending:" , alist)


print("count of 10:", alist.count(10))

getindex= alist.index(20) 
print("index of 20 :",getindex)

# reverse happens in-place
alist.reverse()
print (alist)

popitem = alist.pop(5)
print("after removing:", popitem)

