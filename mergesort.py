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

merge([38,16,27,39,12,27], 0, 5, [38,16,27,39,12,27])
