from aocd import get_data
import numpy as np

f = get_data(day=1)
f = [[int(i) for i in elf.split("\n")] for elf in f.split("\n\n")]

sums = sorted([sum(e) for e in f], reverse=True)

res1 = sum(sums[:1])

res2 = sum(sums[:3])

print(res1, res2)

