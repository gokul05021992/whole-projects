class gokul:
    def __init__(self):
        a=int(input("enter the a value"))
        b=int(input("enter the b value"))
        self.a=a
        self.b=b
class other(gokul):
    def multiplication(self):
        c=self.a*self.b
        print("the multiplication value is",c)
obj=other()
obj.multiplication()
