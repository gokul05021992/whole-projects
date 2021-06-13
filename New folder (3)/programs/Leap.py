print("leap year program")
A=int(input("enter the year"))
if (A%4)==0 and A%100!=0 or (A%400)== 0:
    print("print is an leap year")
else:
    print("it is not a leap")
