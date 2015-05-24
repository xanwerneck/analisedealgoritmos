
def ssctf(lista, n):
	c = 1
	for x in xrange(n-1, 0, -1):
		if lista[x-1] <= lista[n-1]:
			d = ssctf(lista, x)
			if (d+1) > c:
				c = d + 1
	return c


def sscm(lista):
	maior_tamanho = 0
	for x in xrange(0,len(lista)):
		tamanho = ssctf(lista, x + 1)
		if tamanho >= maior_tamanho:
			maior_tamanho = tamanho
	return maior_tamanho

maior = sscm([9,5,6,3,9,6,4,7])
print 'Maior subsequencia: ' + str(maior)
