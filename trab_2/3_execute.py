from instances import instances
from brute_force import less_distance_b_force
import time

def execute_b_force():
	instances_generated = instances()
	for x in xrange(0, len(instances_generated)):
		ini = time.time()
		closest = less_distance_b_force(instances_generated[x])
		fim = time.time()
		print "Tempo de execucao: ", fim-ini
		print "Par de pontos mais proximo: ", closest

execute_b_force()