from aocd import get_data
import numpy as np

f = get_data(day=4)
f = np.array([[list(map(int, i.split("-"))) for i in elf.split(",")] for elf in f.split("\n")])

get_diffs = lambda mtx: np.diff(mtx, axis=0)[0]
is_diffs_contained = lambda nda, mask=[-1, 1]: np.all(nda*mask>=0) or np.all(nda*mask<=0)
is_pairs_contained = lambda mtx, mask=[-1, 1]: is_diffs_contained(get_diffs(mtx), mask=mask)

overlap = lambda mtx: not ((mtx[0][1] < mtx[1][0]) or (mtx[1][1] < mtx[0][0]))

[print(i, get_diffs(i), is_pairs_contained(i), overlap(i)) for i in f]

print(sum([is_pairs_contained(i) for i in f]))
print(sum([overlap(i) for i in f]))

