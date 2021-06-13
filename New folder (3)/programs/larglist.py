l=[10,7,1,12,56,19]
print(l)
l.sort()
print("sorted version of l is",)
print(l)
m=[10,23,65,27,34]
print(m)
if(m[0]>m[1] and m[0]> m[2] and m[0]>m[3] and m[0]>m[4]):
    print(m[0], "is greatest")
elif(m[1]>m[0]) and m[1]>m[2] and m[1]>m[2] and m[1]>m[4]:
    print(m[1],"is greatest")
elif(m[2]>m[0]) and m[2]> m[1] and m[2]> m[3] and m[2]>m[4]:
    print(m[2], "is greatest")
elif(m[3]>m[0]) and m[3]>m[1] and m[3]>m[2] and m[3]>m[4]:
    print(m[3], "is greatest")
else:
    print(m[4],"greatest")

