from distance_compute import distance
import time

def less_distance_b_force(plan):
	ini = fim = time.time()
	closest       = distance(plan[0], plan[1])
	closest_point = [plan[0],plan[1]]
	for i in xrange(0,len(plan)):
		for j in xrange(0,len(plan)):
			if (fim - ini) < 180:
				if i != j:
					dist = distance(plan[i], plan[j])
					if dist < closest:
						closest       = dist
						closest_point = [plan[i],plan[j]]
				fim = time.time()
			else:
				return null
	return distance(closest_point[0], closest_point[1])


#plan = [
#[1,2],
#[3,8],
#[2,1],
#[3,7],
#[8,9],
#[2,6],
#[3.5,7],
#[3.4,7]
#]
#
#ini = time.time()
#closest = less_distance_b_force(plan)
#fim = time.time()
#print "------ Algoritmo de forca bruta ------"
#print "Tempo de execucao: ", fim-ini
#print "Par de pontos mais proximo: ", closest