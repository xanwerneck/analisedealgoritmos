from math import sqrt

class Pair:
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2

  def distance(self):
    return distance(self.point1, self.point2)

  # A pair is greater than other if its distance is bigger
  def __gt__(self, pair):
    return self.distance() > pair.distance()

  # A pair is equal other if both distances are equal
  def __eq__(self, pair):
    return self.distance() == pair.distance()

  def __str__(self):
    return "(" + str(self.point1[0]) + " , " + str(self.point1[1]) + ") <-> (" + str(self.point2[0]) + " , " + str(self.point2[1]) + ")"

def distance(point_a, point_b):
  xa = point_a[0]
  ya = point_a[1]
  xb = point_b[0]
  yb = point_b[1]
  cateto_first  = (xb - xa)**2
  cateto_second = (yb - ya)**2
  return sqrt(cateto_first + cateto_second)
