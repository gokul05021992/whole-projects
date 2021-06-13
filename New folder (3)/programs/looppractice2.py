#loop
l=[]
a=int(input("enter the numbers for element in list to add"))
for i in range(a):
    d=int(input("enter the array value"))
    l.append(d)
print(l)
for j in l:
    if j>100:
        break
    elif j%5==0:
        print(j)
 #loop


