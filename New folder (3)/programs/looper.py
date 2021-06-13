def loop():
    for i in range(0,4):
        for j in range(0,i+1):
            print(j,end='')
        print()
data = int(input("enter the integer :"))
for i in range(data+1):
    t=i*i
print(t)