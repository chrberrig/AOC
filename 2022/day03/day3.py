from aocd import get_data
import numpy as np

f = get_data(day=3)
f = f.split("\n")

mid = lambda s : int(len(s)/2)
mid_sp = lambda s : (s[:mid(s)], s[mid(s):])

f_sp = list(map(mid_sp, f)) # pt1
f_gr = list(zip(*[[f[i] for i in range(len(f)) if i%3==j] for j in range(3)])) # pt2

in_all = lambda cs: list(set(cs[0]).intersection(*[set(c) for c in cs[1:]]))[0]
both_compart = [in_all(cs) for cs in f_sp] # pt1
badges = [in_all(gr) for gr in f_gr] # pt2

priority = lambda s: ((ord("a")<=ord(s)<=ord("z"))*(ord(s)-ord("a")+1) 
        + (ord("A")<=ord(s)<=ord("Z"))*(ord(s)-ord("A") + 27))

prios = list(map(priority, both_compart)) # pt1
prios2 = list(map(priority, badges)) # pt2

#[print(i, j) for i, j in zip(both_compart, prios)]
# [print(gr) for gr in  zip(f_gr, badges, prios2)]

print(sum(prios))
print(sum(prios2))
