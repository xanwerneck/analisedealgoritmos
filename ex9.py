import math

def raizmenores(lista):
	busca = int(math.sqrt(len(lista)))
	result = [0] * busca
	i = 0
	while busca > 0:
		menor = lista[0]
		novalista = []
		for x in xrange(0,len(lista)):
			if lista[x] < menor:
				menor = lista[x]
		result[i] = menor
		for x in xrange(0,len(lista)):
			if lista[x] != menor:
				novalista.append(lista[x])
		i = i + 1
		lista = novalista
		busca = busca - 1
	print result

raizmenores([1,4,3,6,8,5,2,4,5,78,23,21,56,34,22,89,44,33,27,65,34,2,3,9,43,23])