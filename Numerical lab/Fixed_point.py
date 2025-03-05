import sympy as sp

def fixed_point(g_str, ini_guess, tolerance = 1e-6, max_iteration = 100):
  x = sp.symbols('x')
  g = sp.lambdify(x, sp.sympify(g_str), 'numpy')

  x_value = ini_guess
  for i in range (max_iteration):
    x_new = g(x_value)

    if abs(x_new - x_value) < tolerance:
      return x_new, i+1
    x_value = x_new
  
  raise ValueError("Fixed point iteration didn't converge within the maximum number of iterations. ")

if __name__ == "__main__":
  g_str = input("Enter the function g(x) (e.g : x**3-x-2): ")
  initial_guess = float(input("Enter the initial guess : "))

  try:
    root, iter = fixed_point(g_str, initial_guess)
    print(f"Root : ",root)
    print(f"Iterations : ",iter)
  except ValueError as e :
    print(e)
