 
def calc(x, n, tot):
	if n == 1:
		return tot * x
	else:
		if n%2 == 0:
			return calc(x*x, n/2, tot)
		else:
			return calc(x*x, n/2, tot) * x
 
res = calc(2, 10, 1)
print res
res = calc(2, 5, 1)
print res