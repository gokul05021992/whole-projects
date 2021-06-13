from threading import *
import time
def square(n):
    for x in n:
        time.sleep(1)
        x%2
        print("from square function")

def cube(n):
    for x in n:
        time.sleep(1)
        x%3
        print("from cube function")
n=[1,2,3,4]
start=time.time()
t1=Thread(target=square,args=(n,))
t2=Thread(target=cube,args=(n,))

t1.start()
t2.start()

end=time.time()

compiletime=end-start

print(compiletime)