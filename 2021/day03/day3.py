from aocd import get_data
import numpy as np

f = get_data(day=3)
f = np.array([list(int(i) for i in x) for x in f.split("\n")])

roundi = lambda n: (n%1 >= .5)*int(n+1) + (n%1 < .5)*int(n)

print(roundi(0.4))
print(roundi(0.5))
print(roundi(0.6))

# pt. 1
gr = [roundi(x) for x in np.sum(f, axis=0)/np.shape(f)[0]]
er = [1-x for x in gr]
g_int = int("".join([str(x) for x in gr]),2)
e_int = int("".join([str(x) for x in er]),2)
print(g_int, e_int)
print(g_int*e_int)

# pt. 2
filt = lambda l, ref, x: l[x]==ref[x]

most = lambda l: [roundi(x) for x in np.sum(l, axis=0)/np.shape(l)[0]]
least = lambda l: [1-x for x in most(l)]

def seq_filt(ref_fun, coord, l=f):
	l = np.array(l)
	ref = ref_fun(l)
	l = list(filter(lambda l: filt(l, ref, coord), l))
	[print(i) for i in l]
	print(len(l))
	if len(l) == 1:
		return l
	else:
		return seq_filt(ref_fun, coord+1, l)

res_g = int("".join([str(x) for x in seq_filt(most, 0, f)[0]]), 2)
res_e = int("".join([str(x) for x in seq_filt(least, 0, f)[0]]), 2)

print(res_g, res_e)
print(res_g*res_e)
