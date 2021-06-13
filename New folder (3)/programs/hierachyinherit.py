class A_BASE:
    def a(self):
        print(self)
        H=int(input("enter the value of H"))
        self.H=H
        print("the value of H",H, self.H)
class b(A_BASE):
    def ab(self):
        T=int(input("enter the value of B"))
        self.T=T
        print("the value of t", T)

class c(A_BASE):
    def g(self):
        m=int(input("enter the value of m"))
        self.age=m
        print("the value of m", m)
class d(A_BASE):
    def n(self):
        v=int(input("enter the value of v" ))
        self.v=v
        print("the value of v", v)
obj=b()
obj.a()
print(obj.H)

obj1 = b()
obj1.a()
print(obj1.H)

print(obj.H, obj1.H)
# print(vars())

# b.a(obj)
# print(vars(obj))
# obj.ab()
# obj1= c()
# obj1.g()
# obj2= d()
# obj2.n()


