import sympy as sp

def simpsons_rule(func, a, b, n):
    x = sp.Symbol('x')
    f = sp.lambdify(x, func)

    if n % 2 != 0:
        raise ValueError("Number of intervals (n) must be even")
    h = (b - a)/n
    result = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            result += 2*f(x_i)
        else:
            result += 4*f(x_i)

    result *= h/3
    return result

expr = input("Enter the function in terms of x (e.g., x**2 + 3*x ): ")
a = float(input("Enter the lower limit of integration : "))
b = float(input("Enter the upper limit of integration : "))
n = int(input("Enter the number of intervals (must be even) : "))

func = sp.sympify(expr)

try:
    integral = simpsons_rule(func, a, b, n)
    print(f"Integral value using Simpson's Rule: ",integral)
except Exception as e:
    print(f"Error : ",e)