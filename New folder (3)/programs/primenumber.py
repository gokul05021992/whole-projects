H=int(input("enter the number"))
if(H>1):
    if (H%2)==0 or (H%3)==0:
        print("the number is not a prime")
    else:
        print("it is a prime number")
else:
    print("it is not a prime")