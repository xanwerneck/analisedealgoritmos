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

deslocamento([1,2],[1,2,4,1,2,2,1,2])
			