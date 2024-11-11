from aocd import get_data
import numpy as np

f = get_data(day=1)
f = [int(i) for i in f.split("\n")]
x = np.array(f)
f = sum([i>0 for i in np.diff(x[2:] + x[1:-1] + x[:-2])])


print(f)

