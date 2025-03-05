import sympy as sp

def Newton_rapson(func_str,initial,toler=1e-6,max_iter=100):
	
	x = sp.symbols('x')
	
	func = sp.sympify(func_str)
	
	deriv = sp.diff(func,x)
	
	func_callable = sp.lambdify(x, func, 'numpy')
	deriv_callable = sp.lambdify(x, deriv, 'numpy')
	
	x_value = initial
	for i in range(max_iter):
		fx = func_callable(x_value)
		dfx = deriv_callable(x_value)
		
		if dfx == 0:
			raise ValueError("Derivative is zero. No solution found")
		
		x_new = x_value - fx/dfx
		
		if abs(x_new-x_value) < toler :
			return x_new, i+1
			
		x_value = x_new
	raise ValueError("Newton-Rapson did not converge within the maximum number of iterations. ")
		
		
if __name__ == "__main__" :
	func_str = input("Enter the function (e.g : x**3-x-2) : ")
	initial_guess = float(input("Enter the initial guess : "))
	
	try:
		root, iterations = Newton_rapson(func_str,initial_guess)
		print(f"Root : ",root)
		print(f"Iterations : ",iterations)
	except ValueError as e :
		print(e)
