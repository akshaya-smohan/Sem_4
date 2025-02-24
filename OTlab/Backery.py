from scipy.optimize import linprog

c = [-5, -3]

A = [
[2, 1],
[1, 1]
]

b= [500, 1200]

x_bounds = (100, None)
y_bounds = (50, None)
bounds = [x_bounds, y_bounds]

result = linprog(c, A_ub= A,b_ub=b,bounds=bounds, method='highs')

if result.success:
	chocolatecakes = result.x[0]
	vanillacakes = result.x[1]
	max_profit = -result.fun
	
	print(f"Otimal number of chocolatecakes : ",chocolatecakes)
	print(f"Otimal number of vanillacakes : ",vanillacakes)
	print(f"Maximum profit : $",max_profit)
else:
	print("No solution found")
