from order_plan import order_by_x

def div_and_conquer(plan):
	plan = order_by_x(plan)
	print plan



plan = [
[1,2],
[3,8],
[2,1],
[3,7],
[8,9],
[2,6],
[3.5,7],
[3.4,7],
[1,5]
]

div_and_conquer(plan)

