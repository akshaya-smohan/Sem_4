from scipy.optimize import linprog

c = [-20, -30]

A = [
[1, 5],
[3, 1]
]

b= [125,80]

x_bounds = (0, None)
bounds = [x_bounds, x_bounds]

result = linprog(c, A_ub= A,b_ub=b,bounds=bounds, method='highs')

if result.success:
	num_chairs = result.x[0]
	num_tables = result.x[1]
	max_profit = -result.fun
	
	print(f"Otimal number of chairs : ",num_chairs)
	print(f"Otimal number of tables : ",num_tables)
	print(f"Maximum profit : $",max_profit)
else:
	print("No solution found")
