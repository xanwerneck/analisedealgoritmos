# valido para vetores com valores inteiros

def deslocamento(m,n):
	x = len(m) - 1
	operador = 1
	valor = valor_a = 0
	while x >= 0:		
		valor = valor + (m[x] * operador) # valor em decimal do vetor menor		
		valor_a = valor_a + (n[x] * operador) # valor em decimal do vetor maior
		operador = 10 * operador
		x = x - 1

	if valor == valor_a:
		print 0
	operador = operador / 10
	for x in xrange(0,len(n) - len(m)):
		val = ((valor_a % operador) * 10) + n[x + len(m)]
		valor_a = val
		if val == valor:
			print x + 1

def deslocamentoorig(m,n):
	igual = 0
	for x in xrange(0, (len(n)-len(m)) + 1):
		igual = 0
		for y in xrange(0, len(m)):
			if m[y] == n[x+y]:
				igual += 1
		if igual == len(m):
			print x

deslocamentoorig([1,2],[1,2,4,1,2,2,1,2,3,5,2,1,2])
#deslocamento([1,2],[1,2,4,1,2,2,1,2])
			