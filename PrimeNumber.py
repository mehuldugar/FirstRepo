x=int(input("Enter a number you want to check :  "))
if (x > 1):
    for i in range(2,x):
        if (x % i==0): 
            print(x, "not a prime number")
            break
            
    else:print(x, "is a prime number" )
else: print(x, "not a prime number")
