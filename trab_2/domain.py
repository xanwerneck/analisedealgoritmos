from math import sqrt

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "(%.3f , %.3f)" % (self.x, self.y)

class Pair:
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2

  def distance(self):
    cateto_first  = (self.point1.x - self.point2.x)**2
    cateto_second = (self.point1.y - self.point2.y)**2
    return sqrt(cateto_first + cateto_second)

  # Um par eh maior que outro se sua distancia eh maior
  def __gt__(self, pair):
    return self.distance() > pair.distance()

  # Dois pares sao iguais se suas distancias forem iguais  
  def __eq__(self, pair):
    return self.distance() == pair.distance()

  def __str__(self):
    return str(self.point1) + " and " + str(self.point2)
