from instances import each_instance_group
from brute_force import less_distance_b_force
from divide_and_conquer import less_distance_d_conquer
import time

PAIRS_COMPUTED = {\
  less_distance_b_force:   {(25*2**i):[None]*10 for i in xrange(0,12)},\
  less_distance_d_conquer: {(25*2**i):[None]*10 for i in xrange(0,12)}\
}

def execute_b_force(instances_group, qnt_points):
  run_benchmark(instances_group, qnt_points, less_distance_b_force)

def execute_d_conquer(instances_group, qnt_points):  
  run_benchmark(instances_group, qnt_points, less_distance_d_conquer)

def run_benchmark(instances_group, qnt_points, closest_pair):
  print "Usando %d pontos: (Tempo / Distancia)" % qnt_points
  medium_time = 0
  for i in xrange(0, 10):
    ini = time.time()
    closest = closest_pair(instances_group[i])
    PAIRS_COMPUTED[closest_pair][qnt_points][i] = closest
    fim = time.time()
    instance_time = fim-ini
    medium_time += instance_time / 10.0
    if closest is None:
      print "  %.3f / ---" % instance_time
    else:
      print "  %.3f / %.7f" % (instance_time, closest.distance())
  print "  Tempo medio: %.3f" % medium_time

def verify_distances():
  difference_found = False
  for i in xrange(0,12):
    for j in xrange(0,10):
      bforce_pair = PAIRS_COMPUTED[less_distance_b_force][25*2**i][j]
      dconquer_pair = PAIRS_COMPUTED[less_distance_d_conquer][25*2**i][j]
      if not(bforce_pair is None) and not(dconquer_pair is None) and abs(bforce_pair.distance() - dconquer_pair.distance()) >= 0.001:
        print "  Different distances were found: %.7f / %.7f" % (bforce_pair.distance(), dconquer_pair.distance())
        difference_found = True
  if not difference_found:
    print "  All calculated distances are equal"

print "---- Algoritmo de forca bruta ----"
each_instance_group(execute_b_force)
print "---- Algoritmo de divisao e conquista ----"
each_instance_group(execute_d_conquer)

print "---- Verifying if computed distances are the same ----"
verify_distances()
