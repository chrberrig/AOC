from aocd import get_data
import numpy as np
from itertools import permutations

f = get_data(day=5)
f = np.array([[tuple([int(i) for i in y.split(",")]) for y in x.split(" -> ")] for x in f.split("\n")])
# [print(x) for x in f]
latt = np.zeros((1000,1000))

#pt1:
hv_filt = lambda l: np.any(l[1] - l[0] == 0)
hv = list(filter(hv_filt,f))
diffs_hv = [x[1] - x[0] for x in hv]

for line, diff in zip(hv, diffs_hv):
	m = abs(max(diff, key=abs))
	#direct = [int(y) for y in diff/m]
	#trace = [i*direct for i in range(m+1)]
	trace = [[int(y) for y in i*diff/m] for i in range(m+1)]
	lay = [tuple(line[0] + t) for t in trace]
	for l in lay:
		latt[l] += 1

overlaps = list(zip(*np.where(latt>1)))
print(len(overlaps))

#pt2:
diag_filt = lambda l: np.all(np.absolute(l[1] - l[0]) == np.absolute(l[1]-l[0])[0])
diag = list(filter(diag_filt,f))
diffs_diag = [x[1] - x[0] for x in diag]
for line, diff in zip(diag, diffs_diag):
	m = abs(max(diff, key=abs))
	#direct = [int(y) for y in diff/m]
	#print(direct)
	#trace = [i*direct for i in range(m+1)]
	trace = [[int(y) for y in i*diff/m] for i in range(m+1)]
	lay = [tuple(line[0] + t) for t in trace]
	for l in lay:
		latt[l] += 1

overlaps = list(zip(*np.where(latt>1)))
#13018 appearently not correct...
print(len(overlaps))

print(len(hv), len(diag), len(f))
