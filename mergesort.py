def merge(lista, inicio, final, novalista):
	if inicio == final:
		return inicio
	pivot = (final - inicio) / 2
	esquerda = merge(lista, inicio, pivot, novalista)
	direita  = merge(lista, pivot + 1, final, novalista)
	if lista[esquerda] > lista[direita]:
		valor = novalista[direita]
		novalista[direita] = novalista[esquerda]
		novalista[esquerda] = valor
	print novalista

def merge_improve(lista, i, j):
	pivot = (j - i) / 2
	merge_improve(lista, i, pivot)
	merge_improve(lista, pivot+1, j)

merge([38,16,27,39,12,27], 0, 5, [38,16,27,39,12,27])
