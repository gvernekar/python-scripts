ipaddress = input("enter any IP address: ")
ab = ipaddress.split('.')
if(len(ab) != 4) :
    print("Invalid IP")
if(len(ab) == 4):
    if(int(ab[0]) in range(0,255)) :
        if(int(ab[1]) in range(0,255)):
            if(int(ab[2]) in range(0,255)):
                if(int(ab[3]) in range(0,255)):
                    print("Valid IP") 
                    