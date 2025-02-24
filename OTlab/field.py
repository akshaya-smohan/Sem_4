from scipy.optimize import linprog

c = [-200, -150]

A = [
[1, 1],
[20, 10],
[10, 15]
]

b= [60, 1200, 600]

x_bounds = (20, None)
y_bonds = (10, None)
bounds = [x_bounds, y_bounds]

result = linprog(c, A_ub= A,b_ub=b,bounds=bounds, method='highs')

if result.success:
	wheat = result.x[0]
	barley = result.x[1]
	max_profit = -result.fun
	
	print(f"Otimal number of wheat : ",wheat)
	print(f"Otimal number of barley : ",barley)
	print(f"Maximum profit : $",max_profit)
else:
	print("No solution found")
