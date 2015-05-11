import math
import itertools

class _nodes:
  def __init__(self):
    self.perms = itertools.permutations([1,2,3,4,5,6,7,8,0])

  def __iter__(self):
    return self

  def next(self):
    digits = self.perms.next()
    return digits[0]*100000000 + digits[1]*10000000 + digits[2]*1000000 + digits[3]*100000 + digits[4]*10000 + digits[5]*1000 + digits[6]*100 + digits[7]*10 + digits[8]
