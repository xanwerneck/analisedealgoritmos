from graph_base import adjacents, nodes
from graph_stack import graphstack

def create_graph():
	graph = []
	for state in nodes():
		graph.append(state)
	return dfs(graph)

def dfs(graph):
	visited = {}
	trees   = []
	for x in xrange(0,len(graph)):
		if visited.get(graph[x]) == None:
			tree  = graphstack()
			dfs_visit(graph, graph[x], tree, visited)
			trees.append(tree)
	return trees

def dfs_visit(graph, node, tree, visited):	
	visited[node] = 1
	for node_adj in adjacents(node):
		if visited.get(node_adj) == None:
			tree.push(node_adj)
			dfs_visit(graph, node_adj, tree, visited)

visit = create_graph()
print len(visit)
for x in xrange(0, len(visit)):
	print "-------- TREE "
	visit[x].print_tree()
