#basic python
def simple(g,h):
    m=g-h
    print(m)
    print("\n" "welcome")
    n=int(input("enter the first value"))
    s=int(input("enter the second value"))
    print( n,"\n",s)
    print("the multiplication value of 10 and 20 is",n*s)
    print("the average two value is",n*s%2==0)
    return m
def one(r,e):
    m = r * e
    t = r + e
    if m > 1000:
        print (t)
    else:
        print(m,"is not greater than thousand")
r = int(input("enter the value 1"))
e = int(input("enter the value 2"))
one(r,e)