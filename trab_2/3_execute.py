from instances import instances
from brute_force import less_distance_b_force
from divider_and_conquer import less_distance_d_conqueer
import time

def execute_b_force(instances_generated):
  #for x in xrange(0, len(instances_generated)):
  for x in xrange(0, 30):
    ini = time.time()
    closest = less_distance_b_force(instances_generated[x])
    fim = time.time()
    print "Numero de pontos sorteados: ", len(instances_generated[x])
    print "Tempo de execucao: ", fim-ini
    print "Par de pontos mais proximo: ", closest
    print "Distancia: ", closest.distance()

def execute_d_conqueer(instances_generated):  
  #for x in xrange(0, len(instances_generated)):
  for x in xrange(0, 30):
    ini = time.time()
    closest = less_distance_d_conqueer(instances_generated[x])
    fim = time.time()
    print "Numero de pontos sorteados: ", len(instances_generated[x])
    print "Tempo de execucao: ", fim-ini
    print "Par de pontos mais proximo: ", closest
    print "Distancia: ", closest.distance()

instances_generated = instances()
print "---- Algoritmo de forca bruta ----"
execute_b_force(instances_generated)
print "---- Algoritmo de divisao e conquista ----"
execute_d_conqueer(instances_generated)
