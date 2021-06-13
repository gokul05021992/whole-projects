#inheritance->inherite the properties fron one class to another class
#single inheritance
class a:
    def __init__(self):
        a=int(input("Enter the a value:"))
        b=int(input("Enter the b value:"))
        self.a = a
        self.b = b

class b(a):
    def addition(self):
        c=self.a+self.b
        print("Addition value is:",c)

obj1=b()

obj1.addition()