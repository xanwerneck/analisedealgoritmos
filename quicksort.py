def quicksort(lista, pivot, right, nova_lista):
	if pivot < right:
		lim = Partition(lista, pivot, right, nova_lista);
		lista = nova_lista
		print pivot
		print lim + 1

		quicksort(lista, pivot, lim+1, nova_lista);
		#quicksort(lista, lim+1, right, nova_lista);
	print lista


def Partition(lista, pivot, right, nova_lista):
	j = pivot
	k = right - 1
	for x in xrange(pivot,right):
		if lista[x] < lista[pivot]:
			nova_lista[j] = lista[x]
			j = j + 1
		else:
			nova_lista[k] = lista[x]
			k = k - 1
	return k



quicksort([3,5,2,6,1],0,5,[3,5,2,6,1])
quicksort([3,5,2,6,1],0,5,[3,5,2,6,1])

