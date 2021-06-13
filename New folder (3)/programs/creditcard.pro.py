import sys
import calendar
from datetime import *
import datetime
class apply_creditcard:
    def __init__(self):
        self.name=input("enter your name: ")
        self.age=int(input("enter your age: "))
        self.salary=int(input("enter your salary: "))
        self.contact=int(input("enter your 10 digit mobile number: "))
    def process_eligible(self):
        self.min_salary=20000
        self.elage=21
        if self.age<50 and self.age>self.elage:
            if self.salary>self.min_salary:
                print("you are eligible for credit card")
                print("below is your info","\n",self.name,"\n",self.age,"\n",self.salary,"\n",self.salary)
            else:
                print("you are not eligibile")
        else:
            print("you are not eligibile")


    def credit_paymentprocess(self):
        print("credit card bill payment billing date is 22nd of every month")
        self.cusname=input("enter your name")
        self.amt=int(input("enter your billed amt"))
        self.minpay=(self.amt*5)/100
        tday=date.today()
        print(tday)
        user = input("enter the date (please enter the date in this order year-month-date: ")
        print(user)
        user=datetime.datetime.strptime(user,'%Y-%m-%d').date()
        delta=tday-user
        s=delta.days
        if delta.days >20:
            print("you exceeded the due date so you have pay with fine of 700 with  interest")
            m=700+self.minpay
            print(m)
        else:
            print("pay your",self.amt)



app=apply_creditcard()
app.process_eligible()
app.credit_paymentprocess()










