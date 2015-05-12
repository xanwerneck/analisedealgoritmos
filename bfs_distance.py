def bfs(s):
	stack = []
	visited = {}
	distance = {}
	visited[s] = 1
	stack.append(s)
	dist = 0
	while(len(stack)) > 0:
		u = stack.pop()
		distance[u] = dist
		if len(stack) == 0:
			dist += 1

		for w in adj(u):
			if not visited.get(w):
				visited[w] = 1
				stack.append(w)
	print distance

def adj(u):
	graph = [
	  [2, 3],
	  [2],
	  [1, 3],
	  [0]
	]
	return graph[u]

bfs(0)	