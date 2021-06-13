#simple loop
i=0
while i<10:
    print(i)
    i= i+1
#loop addition

for t in range (0,6):
    for j in range(t+1):
        print(j,end=" ")
    print()
#sum of loop
a=int(input("enter the number"))
sum=0
for i in range (0,a+1,1):
    sum=sum+i
    print("sum of ",a ,"is",sum)
#loop multiplication
g=int(input("enter the number for multiply"))
mul=1
for f in range(1,10):
    mul=g*f
print(mul)

