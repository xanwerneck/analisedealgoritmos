
grafo   = [1,2,3,4,5,6,7];
S       = [];
listaAdjElem = [
	[4,5,2],
	[4,6,1],
	[7],
	[5,2,1],
	[1,4,7],
	[2],
	[3,5]
]
d      = [];

def busca(origem):
	for x in xrange(0, len(grafo)):
		if grafo[x] != origem:
			dist = buscabfs(grafo, origem, x + 1)
			d.append([x + 1,dist])
	print d

def buscabfs(gr, origem, destino):
	visited = [0,0,0,0,0,0,0];
	Adiciona(S, origem)
	visited[origem - 1] = 1
	cont = 0
	while len(S) > 0:
		u = Remove(S)
		listaAdj = listaAdjElem[u - 1]
		cont += 1
		
		for y in xrange(0, len(listaAdj)):
			if visited[listaAdj[y] - 1] == 0:
				if (listaAdj[y] == destino):
					return cont
				else:							
					visited[listaAdj[y] - 1] = 1
					Adiciona(S, listaAdj[y])

def Adiciona(gr, elemento):
	gr.append(elemento);

def Remove(gr):
	retorno = gr[0]
	gr.pop(0)
	return retorno

busca(5)