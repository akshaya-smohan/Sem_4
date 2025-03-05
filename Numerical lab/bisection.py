def bisection(f,a,b,tol=1e-6,max_iter=100):
  if f(a)*f(b)>=0:
    raise ValueError("F(a) and F(b) must have opposite signs .")
  for iteration in range(max_iter):
    c = (a+b)/2
    if abs(f(c))<tol:
      print(f"Root found at x = {c} after {iteration+1} iterations.")
      return c
    if f(a)*f(c)<0:
      b=c
    else:
      a=c
				
  print(f"Maximum iterations reached. No root found within the tolererance.")
  return None

if __name__ == "__main__":
  import math
  func_str=input("Enter the function F(x) (use 'x' as the variable, eg: x**3-x-2) : ")
  func = eval(f"lambda x:{func_str}")
  a=float(input("Enter the lower bound of the interval (a) : "))
  b=float(input("Enter the upper bound of the interval (b) : "))
  tol=float(input("Enter the tolerance (eg : 1e-6) : "))
  max_iter=int(input("Enter the maximum number of iterations : "))
  try:
    root = bisection(func,a,b,tol,max_iter)
    if root is not None:
      print(f"Approximate root : {root}")
  except Exception as e:
    print(f"Error : {e}") 
