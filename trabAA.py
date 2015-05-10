lista = []
n = 9

def geraconjuntos(conj, p2):
	if len(conj)==0:
		n_p2 = p2[:]
		lista.append(n_p2)
	else:
		for x in xrange(0,len(conj)):
			p2[n-len(conj)] = conj[x]
			geraconjuntos(df(conj, conj[x]), p2)

def df(cj,y):
	b = []
	for x in xrange(0,len(cj)):
		if cj[x] != y:
			b.append(cj[x])
	return b

geraconjuntos(["0","1","2","3","4","5","6","7","8"], ["","","","","","","","",""])
print len(lista)