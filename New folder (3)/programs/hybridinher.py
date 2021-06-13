class gokul:
    def function1(self):
        print("this is class")
class goks(gokul):
    def function2(self):
        print("this is class one")
class goks1(gokul):
    def function3(self):
        print("this is class two")
class goks2(goks,goks1):
    def function4(self):
        print("this is class three")
obj=goks()
obj.function1()
obj.function2()
obj1=goks1()
obj1.function3()
obj2=goks2()
obj2.function4()



