def buble(lista):
	for x in xrange(0,len(lista)-1):
		if lista[x] > lista[x+1]:
			orig = lista[x]
			lista[x] = lista[x + 1]
			lista[x + 1] = orig
			return buble(lista)
	return lista 


def bubblesort(lista):
	troca = True
	while troca:
		troca = False
		for x in xrange(0,len(lista)-1):
			if lista[x]>lista[x+1]:
				org        = lista[x+1]
				lista[x+1] = lista[x]
				lista[x]   = org
				troca  = True
	print lista


bubblesort([10,2,5,3,1,8])
#nova_lista = buble([10,2,5,3,1,8])
#print nova_lista
