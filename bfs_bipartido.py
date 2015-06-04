import copy

def bfs(s):
	stack = []
	visited = {}
	distance = {}
	layers = []
	layer  = []
	visited[s] = 1
	stack.append(s)
	dist = 0
	while(len(stack)) > 0:
		u = stack.pop()
		distance[u] = dist
		if len(stack) == 0:
			dist += 1
			layers.append(copy.copy(layer))
			layer = []
		else:
			layer.append(u)

		for w in adj(u):
			if not visited.get(w):
				visited[w] = 1
				stack.append(w)
	print distance
	print layers

def adj(u):
	graph = [
	  [1,2],
	  [0,2],
	  [0,1]
	]
	return graph[u]

bfs(0)	