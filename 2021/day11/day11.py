from aocd import get_data
import numpy as np
import itertools as it

f = get_data(day=11)
f = np.array([[int(l) for l in line] for line in f.split("\n")])

gen_nbrs = list(it.product([0, 1, -1], repeat=2))#.remove((0,0))
gen_nbrs.remove((0, 0))
inside_filt = lambda s: all(0 <= i < m for i, m in zip(s, np.shape(f)))
nbrs = lambda s: list(filter(inside_filt, list(tuple(np.array(s)+np.array(x)) for x in gen_nbrs)))

def flash(s, mtx): 
	tmp_mtx = np.copy(mtx)
	for n in nbrs(s):
		tmp_mtx[n] += 1
	return tmp_mtx

def evolve(mtx, count=0, steps=10):
	if steps==0:
		return mtx, count
	else:
		out_mtx = mtx + np.ones(np.shape(mtx))
		old_mtx = np.copy(mtx)
		while np.any((old_mtx>=9) != (out_mtx>=9)):
			print((old_mtx>=9) != (out_mtx>=9))
			tmp_mtx = np.copy(out_mtx)
			for s in list(zip(*np.where((old_mtx>=9) != (out_mtx>=9)))):
				out_mtx = flash(s, out_mtx)			
				count += 1
			old_mtx = tmp_mtx
		out_mtx[np.where(out_mtx>=9)] = 0
		# print(out_mtx)
		return evolve(out_mtx, count=count, steps=steps-1)

print(f)
res = evolve(f, steps=100)
print(res[0])
print(res[1])
# 1888 too high...
