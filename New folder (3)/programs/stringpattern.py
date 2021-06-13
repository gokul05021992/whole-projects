A=input("enter the string")
length = len(A)
for i in range(length):
    for j in range(i+1):
        print(A[j],end=" ")
    print()
