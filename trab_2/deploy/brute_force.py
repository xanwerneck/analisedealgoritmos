from domain import Pair, Point
import time

TIME_LIMIT_IN_SECS = 180

def less_distance_b_force(plan):
  ini = fim = time.time()
  closest       = Pair(plan[0], plan[1])
  for i in xrange(0,len(plan)):
    for j in xrange(0,len(plan)):
      if (fim - ini) < TIME_LIMIT_IN_SECS:
        if i != j:
          pair = Pair(plan[i], plan[j])
          closest = min(pair, closest)
        fim = time.time()
      else:
        return None
  return closest