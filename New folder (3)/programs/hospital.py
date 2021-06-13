print("----------------------------------------------------------------------------")
print()
print("                   Hospital Admission form                         ")
print()
print("-----------------------------------------------------------------------------")
class admission:
    def getdetails(self):
        a=input("enter your name - ")
        b=int(input("enter your age - "))
        c=input("date of birth - ")
        d=int(input("phone number - "))
        e=input("guaridan name - ")
        f=input("address - ")
        g=input("disease - ")
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.g=g
        print()
class display(admission):
    def dip(self):
        print("NAME :", self.a)
        print()
        print("AGE :", self.b)
        print()
        print("DOB : ", self.c)
        print()
        print("number : ", self.d)
        print()
        print("guardian name : ", self.e)
        print()
        print("address : ", self.f)
        print()
        print("disease : ", self.g)
        print()

obj=display()
obj.getdetails()
print("your informations has been saved and you are forwarded to payment section")
obj.dip()







