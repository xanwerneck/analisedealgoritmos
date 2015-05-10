

def incr(lista, x):
	mult = 1
	soma = 0
	for y in xrange(0, len(lista)):
		for k in xrange(0, y-1):
			mult *= x
		soma += lista[y] * mult
		mult = x
	print soma

def incrlinear(lista, x):
	mult = 1
	soma = 0
	for y in xrange(0, len(lista)):
		if y > 0:
			mult *= x		
		soma += lista[y] * mult
	print soma


incrlinear([1,2,3,4], 2);