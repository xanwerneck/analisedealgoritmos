
def numrepetidos(A,p,r,i):
	if i > 10:
		return
	if p<r:
		lista = Partition(A,p,r,i);
		i = i + 1
		A = lista[0]
		l = lista[1]
		numrepetidos(A,p,l+1,i);
		numrepetidos(A,l+1,r,i);
	print 'NAO'

def Partition(lista, pivot, right,i):
	nova_lista = [0] * right
	j = pivot
	k = right - 1
	for x in xrange(pivot,right):
		if lista[x] < lista[pivot]:
			nova_lista[j] = lista[x]
			j = j + 1
		if lista[x] > lista[pivot]:
			nova_lista[k] = lista[x]
			k = k - 1
		else:
			if x != pivot:
				print 'SIM'
	lista_ret = []
	lista_ret.append(nova_lista)
	lista_ret.append(k)
	return lista_ret

numrepetidos([3,2,4,1,5],0,5,0)