
a=int(input("enter the first value"))
b=int(input("enter the secondary value"))
try:
     d = a/b
     print(b)
except ZeroDivisionError:
    print("please enter the value other then zero")
finally:
    print("Final line!!!")



