def recus(a,b):
    if a>b:
        return a
    else:
        return b
result=recus(10,recus(10,76))
print(result)