import numpy as np

def f(a):
    count = 0
    for i in range(1,a+1):
        if i % 3 == 0 and i % 5 == 0:
            #print(i,end=", ")
            count += 1
        elif i % 3 == 0 or i % 5 == 0:
            continue
        else:
            count += 1
    print(count)
inp = int(input())
f(inp)
