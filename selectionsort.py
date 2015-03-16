def selectionsort(lista):
	pos = 0
	tmp = 0
	for x in xrange(0,len(lista)):
		menor = lista[x]
		for y in xrange(x,len(lista)):
			if lista[y] < menor:
				menor = lista[y]
				pos = y
		tmp = lista[x]
		lista[pos] = tmp
		lista[x] = menor
	print lista

selectionsort([1,6,3,4])