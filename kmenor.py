import math

def kmenor(lista, k):
	menor = 99999
	atual = 0
	while k > 0:
		for x in xrange(0, len(lista)):
			if (lista[x] < menor) and (lista[x] > atual):
				menor = lista[x]
		atual = menor
		menor = 99999
		k -= 1
	return atual

def kesimomenor(lista, k):
	if len(lista) <= 5:
		return kmenor(lista, 5/2)
	else:
		medianas = []
		for x in xrange(0, int(math.ceil(len(lista)/5.0))):
			n_lista = lista[i*5:(i+1)*5] #lista de cada subgrupo [i..5i]
			med_tmp = kmenor(n_lista , int(math.ceil(len(n_lista)/2.0)))
			medianas.append(med_tmp)
		kesimomenor(medianas)


kmenor([1,5,2,8,4,9,3], 2)
