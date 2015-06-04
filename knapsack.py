
def knapsack(n, pesos, valores, W):
	M = dict()
	for w in xrange(0, W):
		M[0, w] = 0
	for x in xrange(1,n):
		for w in xrange(1, W):
			if pesos[x] > w:
				M[x, w] = M[x-1, w]
			else:
				M[x, w] = max(M[x-1, w], valores[x] + M[x-1, w - pesos[x]])	

	return M[n-1, W-1]

ret = knapsack(5,[1,6,18,22,28],[1,2,5,6,7], 11)
print ret