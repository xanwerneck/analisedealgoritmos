import random, decimal
from domain import Point

def instances():
  k = 0
  instances = [None] * 120
  for x in xrange(0, 12):
    for y in xrange(0, 10):
      instances[k] = generate_instance(25*(2**x))
      k += 1
  return instances

def generate_instance(size):
  plan = []
  for x in xrange(0, size):
    ponto = Point(0,0)
    ponto.x = float(decimal.Decimal(str(random.random())))
    ponto.y = float(decimal.Decimal(str(random.random())))
    plan.append(ponto)
  return plan

