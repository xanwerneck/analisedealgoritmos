from random import random
from domain import Point

INSTANCES_CACHE = [None for i in xrange(0, 12)]

def each_instance_group(do_something):
  for i in xrange(0, 4):
    points_qnt = 25*(2**i)
    if INSTANCES_CACHE[i] is None:
      INSTANCES_CACHE[i] = [generate_instance(points_qnt) for j in xrange(0, 10)]
    do_something(INSTANCES_CACHE[i], points_qnt)

def generate_instance(size):
  plan = [None] * size
  for i in xrange(0, size):
    plan[i] = Point(random(),random())
  return plan

