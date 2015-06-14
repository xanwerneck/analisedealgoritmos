from order_plan import order_by_x, order_by_y
from domain import Pair, Point

def less_distance_d_conquer(plan):
  plan = order_by_x(plan)
  return closest_pair(plan)

def closest_pair(plan):
  if len(plan) <= 1:
    return None
  elif len(plan) == 2:
    return Pair(plan[0], plan[1])
  elif len(plan) == 3:
    return min(Pair(plan[0], plan[1]), Pair(plan[1], plan[2]), Pair(plan[0], plan[2]))

  left  = plan[:len(plan)/2]
  right = plan[len(plan)/2:]

  min_left  = closest_pair(left)
  min_right = closest_pair(right)
  closest_pair_known = min(min_left, min_right)

  middle_x = compute_middle_x_of_L(left, right)

  l_points = get_points_in_L(left, right, middle_x, closest_pair_known.distance())
  l_points = order_by_y(l_points)

  for i in xrange(0, len(l_points)-1):
    for j in xrange(i+1, min(i+8, len(l_points))):
      pair = Pair(l_points[i], l_points[j])
      closest_pair_known = min(pair, closest_pair_known)

  return closest_pair_known

def compute_middle_x_of_L(left, right):
  if len(left) == 0: return right[0].x
  if len(right) == 0: return left[-1].x

  return (left[-1].x + right[0].x) / 2

def get_points_in_L(left, right, l_middle_x, l_half_width):
  l_points = []
  for point in left:
    if point.x >= (l_middle_x - l_half_width):
      l_points.append(point)

  for point in right:
    if point.x <= (l_middle_x + l_half_width):
      l_points.append(point)

  return l_points
      
  



#plan = [
# Point(1,2),
# Point(3,8),
# Point(2,1),
# Point(3,7),
# Point(8,9),
# Point(2,6),
# Point(3.5,7),
# Point(3.4,7),
# Point(1,5)
#]
#
#closest_pair = closest_pair(plan)
#print closest_pair
#print closest_pair.distance()
