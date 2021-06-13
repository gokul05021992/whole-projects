#pattern number loop
def tri(rows):
    for i in range(0,rows):
        for j in range(0,i+1):
            print(getnumber(i,j),end=" ")
        print()
def getnumber(x,y):
    num =1
    if y>x-y:
        y=x-y
    for i in range(0,y):
        num = num*(x-i)
        num = num//(i+1)
    return num
c=int(input("enter the value of rows :"))
tri(c)



