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

def selection(lista):
	x = 0
	while x < len(lista):
		menor = lista[x]
		pos = x
		for y in xrange(x+1,len(lista)):
			if lista[y] < menor:
				menor = lista[y]
				pos   = y
		tmp = lista[x]
		lista[x] = lista[pos]
		lista[pos] = tmp
		x += 1
	print lista

selection([1,20,6,0,21,3,4])