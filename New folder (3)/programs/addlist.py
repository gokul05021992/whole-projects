def addlist(list):
    add=0
    for i in list:
        add=add+i   #(add=0+i)
    return add
result=addlist([10,20,30,40,50])
print(result)
n=[]
a=int(input("enter the number of elements:"))

for i in range(0,a):
    e = int(input("Enter the elements:"))
    n.append(e)
print(n)
n.insert(a[10])
print(n)

