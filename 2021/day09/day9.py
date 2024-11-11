from aocd import get_data
import numpy as np
from itertools import permutations

f = get_data(day=9)
f = np.array([list(x) for x in f.split("\n")], dtype=int)
print(f)
print(np.shape(f))
nn = [-1, 1]
unn = lambda s: [tuple([b + (j==i)*k for j, b in enumerate(s)]) for i, e in enumerate(s) for k in nn]
inside = lambda s : np.all([(0<=e<np.shape(f)[i]) for i, e in enumerate(s)])
nbrs = lambda s: list(filter(inside, [(k,l) for k,l in unn(s)]))

# pt1:
lps = []
for i in range(np.shape(f)[0]):
	for j in range(np.shape(f)[1]):
		s = (i, j)
		if np.all([f[s] < f[n] for n in nbrs(s)]):
			lps.append(s)
			print(s, f[s])
print(np.sum([f[s]+1 for s in lps]))

# pt2:
all_basins = []
while len(lps)>0:
	lp = lps.pop()
	actives = [lp]
	basin = []
	while len(actives)>0:
		a = actives.pop()
		for n in nbrs(a):
			if (n not in actives) and (n not in basin) and (f[n]<9):
				actives.append(n)
			if n in lps:
				lps.remove(n)
		basin.append(a)
	all_basins.append(basin)
all_basins.sort(key=len)
for b in all_basins:
	print(b)
print(len(all_basins[-3])*len(all_basins[-2])*len(all_basins[-1]))
