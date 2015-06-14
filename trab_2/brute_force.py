from domain import Pair, Point
import time

def less_distance_b_force(plan):
  ini = fim = time.time()
  closest       = Pair(plan[0], plan[1])
  for i in xrange(0,len(plan)):
    for j in xrange(0,len(plan)):
      if (fim - ini) < 180:
        if i != j:
          pair = Pair(plan[i], plan[j])
          closest = min(pair, closest)
        fim = time.time()
      else:
        return None
  return closest


#plan = [
#  Point(1,2),
#  Point(3,8),
#  Point(2,1),
#  Point(3,7),
#  Point(8,9),
#  Point(2,6),
#  Point(3.5,7),
#  Point(3.4,7)
#]
#
#ini = time.time()
#closest = less_distance_b_force(plan)
#fim = time.time()
#print "------ Algoritmo de forca bruta ------"
#print "Tempo de execucao: ", fim-ini
#print "Par de pontos mais proximo: ", closest
#print "Distancia: ", closest.distance()
