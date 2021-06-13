class fibonicci:
    def __init__(self):
        a=int(input("enter"))
        f=0
        s=1
        for x in range(a):
            next = f + s #1 #2
            print(next)  #1 #2
            f = s   #f=0  f=1
            s = next #s=1 2







ob=fibonicci()
