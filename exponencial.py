 
def calc(x, n):
	if n == 1:
		return x
	else:
		if n%2 == 0:
			return calc(x*x, n/2)
		else:
			return calc(x*x, n/2) * x
 
res = calc(2, 10)
print res
res = calc(2, 5)
print res