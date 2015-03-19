# maior intervalo

def maxintervalorn3(a):
	intervalos = []
	maiorvalor = -99999
	maiorintervalo = []
	for x in xrange(1, len(a)):
		intervalos.append(x)
		intervalos[x-1] = []
		for k in xrange(0,(len(a)-x) + 1):
			intervalo = []
			valor = 0;
			for y in xrange(0,x):
				intervalo.append(a[k + y])
				valor = valor + a[k + y]
			if valor > maiorvalor:
				maiorvalor = valor
				maiorintervalo = intervalo
			intervalos[x-1].append(intervalo)	
	print maiorintervalo	


def maxintervalon2(lista):
	maior = -9999
	for x in xrange(0,len(lista)):
		tmp = lista[x]
		if tmp > maior:
			maior = tmp
		for y in xrange(x+1,len(lista)):
			tmp = tmp + lista[y]
			if tmp > maior:
				maior = tmp
				i = x
				j = y
	maiorintervalo = []
	for x in xrange(i,j+1):
		maiorintervalo.append(lista[x])
	print maiorintervalo

def maxintervalon(lista):
	soma = lista[0]
	maior = lista[0]
	a = b = 0
	for x in xrange(1,len(lista)):
		if lista[x] > 0:
			if (soma + lista[x]) >= lista[x]:
				soma = soma + lista[x]
			else:
				soma = lista[x]
			if soma > maior:
				maior = soma
				if soma == lista[x]:
					a = x		
				b = x	
		else:
			if (soma + lista[x]) >= 0:
				soma = soma + lista[x]
			else:
				soma = lista[x]

	maiorintervalo = []
	for x in xrange(a,b+1):
		maiorintervalo.append(lista[x])
	print maiorintervalo
	#print maior

maxintervalorn3([1,2,-1,3,-5])
maxintervalon2([1,2,-1,3,-5])
maxintervalon([-1,3,-5])
maxintervalon([1,2,-1,3,-5])
maxintervalon([-5,1,2,-5,1,-5])
