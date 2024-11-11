from aocd import get_data
import numpy as np

f = get_data(day=8)
f = np.array([x.split(" | ") for x in f.split("\n")])
f = np.array([[k.split(" "), d.split(" ")] for k, d in f])

lu = lambda d: np.sum([len(n) in [2, 3, 4, 7] for n in d])
c = np.sum([lu(d) for k, d in f])

print(f)
print(c)

# pt. 2:
print(f)
print(c)
