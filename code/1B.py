import numpy as np

def f(s):
    a = s.split(" ")
    tmp = ""
    count = 0
    for i in a:
        if count == 0:
            tmp += i[::-1]
        else:
            tmp += " "
            tmp += i[::-1]
        count += 1
    print(tmp)
f(input())