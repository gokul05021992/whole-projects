from atmreg import *
class atm:
    def amtp(self):
        bal = 1000
        print("bank of baroda")
        print()
        print("press 1 for withdrawal")
        print("press 2 for balance")
        print("press 3 deposit")
        print("press 4 quit")
        wid=int(input("enter your choice below : "))
        self.bal=bal
        self.wid=wid
    def withdraw(self):
        self.retrycount=3
        if self.wid==1 :
            drew=int(input("enter the amount goint to withdraw: "))
            print()
            if drew<=self.bal or drew==self.bal:
                print("widrawal sucess the remaining balance is : ",self.bal-drew)
            else:
                print("insufficient balance")
            self.drew=drew
        elif self.wid==2:
            print("your balance is ", self.bal)
            print()
        elif self.wid ==3:
            dep=int(input("enter the amount going to deposit"))
            print
            print("available balance after deposit is ",dep+self.bal)
            print()
        elif self.wid==4:
            print("thank you for visiting bank of baroda ")
            print()
        else:
            print("incorrect input enter it correctly")
            self.retrycount=-1
            self.retrycount
            if self.retrycount !=0:
                print(self.amtp())
atmp=atm()
atmp.amtp()
atmp.withdraw()



