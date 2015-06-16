from random import random
from domain import Point

INSTANCES_CACHE = [None] * 12

#
# @desc   : itera por cada grupo de 10 instancias
#
# @params : do_something = funcao que processa o grupo de 10 instancias
#
def foreach_instance_group(do_something):
  for i in xrange(0, 12):
    points_qnt = 25*(2**i)
    if INSTANCES_CACHE[i] is None:
      INSTANCES_CACHE[i] = [generate_instance(points_qnt) for j in xrange(0, 10)]
    do_something(INSTANCES_CACHE[i])

def generate_instance(size):
  plan = [None] * size
  for i in xrange(0, size):
    plan[i] = Point(random(),random())
  return plan

