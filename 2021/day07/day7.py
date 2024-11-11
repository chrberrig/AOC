from aocd import get_data
import numpy as np

f = get_data(day=7)
f = np.array([int(x) for x in f.split(",")])
#print(f)
b_min, b_max = min(f), max(f)
# d = [(i, np.sum(abs(i*np.ones(len(f)) - f))) for i in range(b_min, b_max+1)]
# [print(abs(i*np.ones(len(f)) - f)) for i in range(b_min, b_max+1)]
# print(d)
# print(min(d, key=lambda l: l[1]))

# pt. 2
m = 1e15
i_m = 0
for i in range(b_min, b_max+1):
	d = abs(i*np.ones(len(f)) - f)
	s = np.sum(d*(d+1)/2)
	cond = s<m 
	m = (cond)*s + (not cond)*m
	i_m = (cond)*i + (not cond)*i_m
	print(i, s)
print("--"*20)
print(i_m, m)

