
def exponencialcrescente(lista, elem):
	soma = 0
	for x in xrange(0,len(lista)):
		if x == 0:
			mult = 1
		else:
			mult = elem
			for y in xrange(0, x-1):
				mult = mult * elem
		soma = soma + (lista[x] * mult)
	print soma

def exponencialcrescenten(lista, elem):
	soma = 0
	mult = 1
	for x in xrange(0,len(lista)):
		if x == 0:
			mult = 1
		else:
			mult = mult * elem		
		soma = soma + (lista[x] * mult)
	print soma

exponencialcrescente([10,2,5,3], 3)
exponencialcrescente([0,1,2,3], 2)

exponencialcrescenten([10,2,5,3], 3)
exponencialcrescenten([0,1,2,3], 2)