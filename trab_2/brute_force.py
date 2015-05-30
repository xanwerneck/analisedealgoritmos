from distance_compute import distance

def less_distance_b_force(plan):
	closest       = distance(plan[0], plan[1])
	closest_point = [plan[0],plan[1]]
	for i in xrange(0,len(plan)):
		for j in xrange(0,len(plan)):
			if i != j:
				dist = distance(plan[i], plan[j])
				if dist < closest:
					closest       = dist
					closest_point = [plan[i],plan[j]]
	return closest_point


plan = [
[1,2],
[3,8],
[2,1],
[3,7],
[8,9],
[2,6],
[3.5,7],
[3.4,7]
]

closest = less_distance_b_force(plan)
print closest