from math import sqrt

def distance(point_a,point_b):
	xa = point_a[0]
	ya = point_a[1]
	xb = point_b[0]
	yb = point_b[1]
	cateto_first  = (xb - xa)**2
	cateto_second = (yb - ya)**2
	return sqrt(cateto_first + cateto_second)

