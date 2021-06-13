#nothingbut method which behaves differently for different object

class one:
    def sound(self):
        print("bow bow bow")
class two:
    def sound(self):
        print("tik tik tik")

def makesound(call):
    call.sound()
obj1=one()
obj=two()
makesound(obj1)
makesound(obj)