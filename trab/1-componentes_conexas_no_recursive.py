from graph_base import adjacents, nodes

def create_graph():
	# initialize all nodes in a array
	graph = []
	for state in nodes():
		graph.append(state)
	return dfs(graph)

def dfs(graph):
	visited = {} # armazena todos os nos visitados
	trees   = [] # array com as arvores formadas na visita ao no
	for x in xrange(0,len(graph)):
		if visited.get(graph[x]) == None:
			tree = search(graph, graph[x], visited)
			trees.append(tree)
	return trees


def search(graph, nod, visited):
	tree_way = {}     # a lista contem o caminho pela componente conexa
	stack    = []     # pilha para eliminar as recursoes
	stack.append(nod) # inicia a pilha com o no de entrada

	while(len(stack) > 0):
		node = stack.pop()
		for node_adj in adjacents(node):
			if not tree_way.get(node_adj) and not visited.get(node_adj):
				stack.append(node_adj)
		tree_way[node] = 1
		visited[node]  = 1

	return tree_way



visit = create_graph()
print len(visit)
for x in xrange(0, len(visit)):
	print "-------- Componente conexa "
	#print visit[x].keys()
	print "-------- Qtde vertices"
	print len(visit[x])
	print "-------- Qtde arestas"
	print len(visit[x]) - 1
