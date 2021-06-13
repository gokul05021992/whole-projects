
try:
 nterms = int(input("How many terms? "))
except ValueError:
  nterms = int(input("How many terms? "))
finally:
 n1=0
 n2=1
 count =0
 print("fibonicci sequence")
 if nterms == 1 or 0:
    print("please enter the correct value")
while count < nterms:
     print("the result of ",n2,"and" ,n1,"is:", n1)
     nth=n1+n2 #1
        #updating values
     n1=n2 #1
     n2=nth #2
     count +=1 #1

