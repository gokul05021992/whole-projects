print("-------------------------------------------")
print("             billing section                ")
print("--------------------------------------------")

class billing:
    def bill(self):
        z=int(input("how many days going to stay" ))
        print()
        t=int(input("for general ward press 1 for special ward press 2" ))
        print()
        self.z=z
        self.t=t
    def displ(self):
        m=self.z*100
        g=self.z*50
        if self.t==1:
            print("stay charge is(doctor fees per days is 50 included)", m+50*self.z)
            print()
            r=int(input("enter the amount you goint to pay"))
            print()
            print("remaining pay is",  m+50*self.z-r)
            print()
        else:
            print("stay charge is(doctor fees per days is 50 included)", g+50*self.z)
            print()
            x = int(input("enter the amount you goint to pay"))
            print()
            print("remaining pay is", g+50*self.z - x)
            print()


obj=billing()
obj.bill()
obj.displ()
print("thank you visit again")


