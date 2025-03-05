import math


func_str = input("Enter the function in terms of x (e.g: 'math.sin(x)') : ")
h = float(input("Enter the step size (h) : "))
x = float(input("Enter the point x at which to compute the second derivative : "))

f = lambda x: eval(func_str)

def second_derivative (x,h):
    return ((f(x+h)-2*f(x)+f(x-h))/(h**2))



result = second_derivative(x,h)

print("Second derivative of f(x) is : ",result)