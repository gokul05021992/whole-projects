import sys
print("***********************************************************")
print("              BANK OF BARODA                                ")
print("              REGISTRATION                    ")
class registration:
    def getInput(self):
        self.maxretry = 3
        a=int(input("enter your card number :"))
        print()
        b=int(input("set your pin: "))
        print()
        c=input("enter your name: ")
        print()
        print("pin created for user : ","\n",c,"\n","for the card number ",a,"\n","the pin is  ****")
        print()
        print("take your card and insert again to check")
        self.a=a
        self.b=b
        self.c=c
        print("insert your card")
class readingCard(registration):
    def CardProcess(self):
        m=self.b
        print()
        f=int(input("enter your pin: "))
        print()
        if f==m:
            print("hi",self.c)
        else :
            print("wrong password enter it correctly")
            self.maxretry = self.maxretry - 1
            while self.maxretry!=0:
                print("retry again")
                print(self.CardProcess())
            else:
                print("wrong password exited")
                sys.exit()

get=readingCard()
get.getInput()
get.CardProcess()
