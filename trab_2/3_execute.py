from instances import foreach_instance_group
from brute_force import less_distance_b_force
from divide_and_conquer import less_distance_d_conquer
import time


#
# @const  : Estrutura de dados usada para guardar todos os resultados
#           obtidos com o brute force e divide and conquer afim de
#           compara-los na funcao verify_distances.
#           Ex.: PAIRS_COMPUTED[less_distance_b_force][25][0] retorna
#           o resultado da primeira instancia de 25 pontos usando brute force.
#
PAIRS_COMPUTED = {\
  less_distance_b_force:   {(25*2**i):[None]*10 for i in xrange(0,12)},\
  less_distance_d_conquer: {(25*2**i):[None]*10 for i in xrange(0,12)}\
}

#
# @desc   : executa o algoritmo para um grupo de 10 instancias e imprime: 
#           tempo de execucao + distancia calculada
# @params : instances_group = grupo de 10 instancias de tamanho 25*2**i
#           closest_pair    = funcao [brute_force ou div_and_conquer] que 
#                             sera usada para calcular o par de pontos
#                             mais proximo
#
def run_benchmark(instances_group, closest_pair):
  qnt_points = len(instances_group[0])
  print "Usando %d pontos: (Tempo / Distancia)" % qnt_points
  medium_time = 0
  distances_sum = 0
  computed_distances = 0
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
      computed_distances += 1
      distances_sum += closest.distance()
      print "  %.3f / %.7f" % (instance_time, closest.distance())
  print "  Tempo medio: %.3f" % medium_time
  if computed_distances == 0:
    print "  Distancia media: ---"
  else:
    print "  Distancia media: %.7f" % (distances_sum / computed_distances)

#
# @desc   : compara se as distancias calculadas por cada algoritmo sao
#           iguais
#
def verify_distances():
  difference_found = False
  for i in xrange(0,12):
    for j in xrange(0,10):
      bforce_pair = PAIRS_COMPUTED[less_distance_b_force][25*2**i][j]
      dconquer_pair = PAIRS_COMPUTED[less_distance_d_conquer][25*2**i][j]
      if not(bforce_pair is None) and not(dconquer_pair is None) and abs(bforce_pair.distance() - dconquer_pair.distance()) >= 0.001:
        print "  Distancias diferentes encontradas: %.7f / %.7f" % (bforce_pair.distance(), dconquer_pair.distance())
        difference_found = True
  if not difference_found:
    print "  Todas as distancias calculadas sao iguais"


print "---- Algoritmo de forca bruta ----"
foreach_instance_group(lambda group:\
  run_benchmark(group, less_distance_b_force)) 

print "---- Algoritmo de divisao e conquista ----"
foreach_instance_group(lambda group:\
  run_benchmark(group, less_distance_d_conquer))

print "---- Verificando se as distancias computadas sao iguais ----"
verify_distances()
