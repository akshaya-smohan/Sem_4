import math

x = math.pi / 4
h = 0.05

def f(x):
    return math.sin(x)

def CDD (x,h):
    return ((f(x+h)-f(x-h))/(2*h))

cdd =CDD(x,h)

print("CDD value of f(x) is : ",cdd)