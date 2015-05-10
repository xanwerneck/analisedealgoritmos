
grafo   = [1,2,3,4,5,6,7];
visited = [0,0,0,0,0,0,0];
S       = [];
listaAdjElem = [
	[4,5,2],
	[4,6,1],
	[7],
	[5,2,1],
	[1,4],
	[2],
	[3]
]

def busca():
	for x in xrange(0,len(grafo)):
		if visited[x] == 0:
			buscaprofundidade(grafo, grafo[x])
	print S

def buscaprofundidade(grafo, v):
	visited[v - 1] = 1
	listaAdj       = listaAdjElem[v - 1]
	for w in xrange(0, len(listaAdj)):
		if visited[listaAdj[w] - 1] == 0:
			S.append([v, listaAdj[w]])
			buscaprofundidade(grafo, listaAdj[w])


busca();