from order_plan import order_by_x, order_by_y
from distance_compute import distance

def get_closest(left, right, median, min_general):
	closest_plan = []
	for x in xrange(0, len(left)):
		if left[x][0] >= (median - min_general):
			closest_plan.append(left[x])

	for x in xrange(0, len(right)):
		if right[x][0] <= (median + min_general):
			closest_plan.append(right[x])

	return closest_plan
			

def computeL(left, right):
	last_left = 0
	if len(left) > 0:
		last_left   = left[len(left) - 1][0]

	first_right = 0
	if len(right) > 0:
		first_right = right[0][0]

	return (last_left + first_right) / 2

def less_distance_d_conqueer(plan):
	plan = order_by_x(plan)
	return closest_pair(plan)

def closest_pair(plan):

	if len(plan) == 1:
		return 999999

	left  = plan[:len(plan)/2]
	right = plan[len(plan)/2:]

	min_left  = closest_pair(left)
	min_right = closest_pair(right)

	median = computeL(left,right)

	min_general = min_left
	if min_general > min_right:
		min_general = min_right

	middle = get_closest(left, right, median, min_general)

	middle_ordered = order_by_y(middle)


	for x in xrange(0, len(middle_ordered)):
		begin = x + 1
		if begin == len(middle_ordered):
			return min_general
		if (begin + 8) - len(middle_ordered) >= 0:
			end = len(middle_ordered)
		else:
			end = begin + 8
		for y in xrange(begin, end):
			dist = distance(middle_ordered[x], middle_ordered[y])
			if dist < min_general:
				min_general = dist

	return min_general
	



#plan = [
#	[1,2],
#	[3,8],
#	[2,1],
#	[3,7],
#	[8,9],
#	[2,6],
#	[3.5,7],
#	[3.4,7],
#	[1,5]
#]
#
#closest_pair = div_and_conquer(plan)
#print closest_pair

