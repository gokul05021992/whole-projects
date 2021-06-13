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
        print("From cube function")
n=[1,2,3,4]

start=time.time()

square(n)

cube(n)

end=time.time()

compiletime=end-start

print(compiletime)
