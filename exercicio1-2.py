

def calc(n):
	a = 0
	cont = 0
	for x in xrange(1,n+1):
		print 'x='+str(x)
		cont= cont+1
		for y in xrange(x+1,n+1):
			print 'y='+str(y)
			cont= cont+1
			for k in xrange(1,(y-x)+1):
				print 'k='+str(k)
				cont= cont+1
				a = a + 1
	print 'resultado de a='+str(a)
	print 'numero de passadas='+str(cont)

calc(3)