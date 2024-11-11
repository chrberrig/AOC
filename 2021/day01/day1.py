from aocd import get_data
import numpy as np

f = get_data(day=1)
f = [int(i) for i in f.split("\n")]
f = sum([i>0 for i in np.diff(np.array(f))])

print(f)

