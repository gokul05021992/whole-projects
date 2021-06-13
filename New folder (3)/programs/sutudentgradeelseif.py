print("student result")
A=int(input("enter your mark"))
if (A>39):
    if(A<60):
        print("you are pass and your grade is D")
    elif(A<80):
        print("you are pass and your grade is C")
    elif(A<90):
         print("your are pass and your grade is B")
    elif(A<100):
         print("congratulation you scored more than 90 and your grade is A")
    elif(A==100):
         print("centum brilliant")
    else:
         print("incorrect data entered enter the correct mark")
else:
    print("your are fail try next time")



