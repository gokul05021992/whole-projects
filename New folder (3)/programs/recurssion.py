#function inside a function is called recurssion

def addition(a,b):
    c=a+b
    return c
result=addition(10,addition(30,40))
print(result)

