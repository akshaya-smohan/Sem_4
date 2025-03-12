import sympy as sp

def trapezoidal_rule(func, a, b, n):
    x = sp.Symbol('x')
    f = sp.lambdify(x, func)

    
    h = (b - a)/n
    result = (f(a) + f(b))/2

    for i in range(1, n):
        x_i = a + i * h
        result += f(x_i)

    result *= h
    return result

expr = input("Enter the function in terms of x (e.g., x**2 + 3*x ): ")
a = float(input("Enter the lower limit of integration : "))
b = float(input("Enter the upper limit of integration : "))
n = int(input("Enter the number of intervals : "))

func = sp.sympify(expr)

try:
    integral = trapezoidal_rule(func, a, b, n)
    print(f"Integral value using Multiple trapezoidal Rule: ",integral)
except Exception as e:
    print(f"Error : ",e)