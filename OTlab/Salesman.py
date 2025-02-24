import math

def tsp_recursive(graph,current_city,visited,n,start_city):
	if len(visited)==n:
		return graph[current_city][start_city]
		
	min_distance = float('inf')
	
	for next_city in range(n):
		if next_city not in visited:
			visited.add(next_city)
			distance = graph[current_city][next_city]+tsp_recursive(graph,next_city,visited,n,start_city)
			
			min_distance = min(min_distance, distance)
			visited.remove(next_city)
	return min_distance
	

def tsp(graph):
	n=len(graph)
	start_city =0
	visited = set([start_city])
	return tsp_recursive(graph,start_city,visited,n,start_city)
	

graph = [
[0, 10, 15, 20],
[10, 0, 35, 25],
[15, 35, 0, 30],
[20, 25, 30, 0]
]

min_distance = tsp(graph)

print("Minimum distance : ",min_distance)
