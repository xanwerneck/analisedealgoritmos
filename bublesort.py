def buble(lista):
	for x in xrange(0,len(lista)-1):
		if lista[x] > lista[x+1]:
			orig = lista[x]
			lista[x] = lista[x + 1]
			lista[x + 1] = orig
			return buble(lista)
	return lista 


nova_lista = buble([10,2,5,3,1,8])
print nova_lista
