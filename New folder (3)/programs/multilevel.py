#level by level inharitance
class grandparaent:
    def get_a(self):
        a=int(input("Enter the a value:"))
        self.a=a
class parent(grandparaent):

    def get_b(self):
        b=int(input("Enter the b value:"))
        self.b=b
class child(parent):
    def display(self):
        print("A value is:", self.a)
        print("B value is:", self.b)


obj = child()
obj.get_a()
obj.get_b()
obj.display()
