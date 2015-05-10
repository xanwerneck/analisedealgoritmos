
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
			Adiciona(S, grafo[x])
			visited[x] = 1
			while len(S) > 0:
				u = Remove(S)
				listaAdj = buscaAdj(u)
				for y in xrange(0, len(listaAdj)):
					if visited[listaAdj[y] - 1] == 0:
						visited[listaAdj[y] - 1] = 1
						Adiciona(S, listaAdj[y])


def Adiciona(grafo, elemento):
	grafo.append(elemento);
	print grafo

def Remove(grafo):
	retorno = grafo[0]
	grafo.pop(0)
	print grafo
	return retorno

def buscaAdj(elemento):
	for x in xrange(0, len(grafo)):
		if elemento == grafo[x]:
			return listaAdjElem[x]


busca();