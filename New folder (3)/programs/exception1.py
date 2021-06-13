try:
    a = int(input("Enter the a value:"))
    print(a)
except ValueError:
    print("Please enter the integer value!!")
finally:
    print("Final line!!!")

print("hi")