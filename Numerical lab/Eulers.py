import sympy as sp

def Eulers_rule(func, x0, y0, x_end, h):
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    f = sp.lambdify((x,y), func)

    n =  int((x_end - x0)/h)
    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        y_new = y0 + h * f(x0, y0)
        x0 += h
        y0 = y_new
        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values

expr = input("Enter the differential equation in terms of x and y (e.g., x + y ): ")
x0 = float(input("Enter the initial value of x : "))
y0 = float(input("Enter the initial value of y : "))
x_end = float(input("Enter the value of x at which to stop : "))
h = float(input("Enter the step size (h) : "))

func = sp.sympify(expr)

try:
    x_vals, y_vals = Eulers_rule(func, x0, y0, x_end, h)
    print("\nResults : ")
    for x, y in zip(x_vals, y_vals):
        print(f"x = {x : 4f}, y = {y : 4f}")
except Exception as e:
    print(f"Error : ",e)
