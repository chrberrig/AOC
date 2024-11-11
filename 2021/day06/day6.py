from aocd import get_data
import numpy as np

# f = np.array([3,4,3,1,2])
f = get_data(day=6)
f = np.array([int(x) for x in f.split(",")])

l = np.array([list(f).count(i) for i in range(8+1)])
def evolve(l, steps=80):
	print(steps, l, np.sum(l))
	if steps==0:
		return l
	else:
		pocket = l[0]
		l[:-1] = l[1:]
		l[6] += pocket
		l[8] = pocket
		return evolve(l, steps=steps-1)
#l = evolve(l, 80)
# pt. 2:
l = evolve(l, 256)
print(np.sum(l))
