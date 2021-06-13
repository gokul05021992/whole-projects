import sys
#from atmreg import *
print("bank of baroda atm")
class atm:
    def atm_card(self):
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
class process(atm):
    def withdrawal(self):
        if self.wid==1 :
            drew=int(input("enter the amount goint to withdraw: "))
            print()
            if drew<=self.bal or drew==self.bal:
                print("widrawal sucess the remaining balance is : ",self.bal-drew)
                self.remaining=self.bal-drew
                self.con=int(input("do you want to continue 1 for main menu or press 2 to cancel "))
                if self.con==1:
                    print(atmo=process())
                else:
                    sys.exit("thank for visiting")
            else:
                print("insufficient balance")
                self.con = int(input("do you want to continue 1 for main menu or press to cancel "))
                if self.con == 1:
                    for i in self.atm_card():
                        print(i)
                else:
                    sys.exit("thank for visiting")


atmo=process()
atmo.atm_card()
atmo.withdrawal()





