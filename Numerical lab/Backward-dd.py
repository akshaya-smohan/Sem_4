import math

x = math.pi / 4
h = 0.05

def f(x):
    return math.sin(x)

def CDD (x,h):
    return ((f(x)-f(x-h))/(h))

bdd =CDD(x,h)

print("BDD value of f(x) is : ",bdd)