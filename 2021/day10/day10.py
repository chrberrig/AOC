from aocd import get_data
import numpy as np

f = get_data(day=10)
f = np.array([x for x in f.split("\n")])
#print(f)
print("len(f)")
print(len(f))
os = ["(", "[", "{", "<"]
cs = [")", "]", "}", ">"]
ps = [3, 57, 1197, 25137]
state = []
errs = []
correct_lines = []
for i, line in enumerate(f):
	saveline = 1
	for j, lett in enumerate(line):
		if lett in os:
			state.append(os.index(lett))
		elif lett==cs[state[-1]]:
			state.pop(-1)
		else:
			# print(f"err, sym:{j}, line: {i}: found {lett}, expected {cs[state[-1]]}")
			errs.append(lett)
			saveline=0
			break
	if saveline:
		correct_lines.append(line)
scores = [ps[cs.index(j)] for j in errs]
#print(scores)
print("len(errs)")
print(len(errs))
print(np.sum(scores))

def fun(l):
	count = 0
	for i in l:
		count = count*5+i
	return count

c_ps = [1, 2, 3, 4]
all_scores = []
for i, line in enumerate(correct_lines):
	c_state = []
	for j, lett in enumerate(line):
		if lett in os:
			c_state.append(os.index(lett))
		elif lett==cs[c_state[-1]]:
			c_state.pop(-1)
	c_state.reverse()
	c_score = [c_ps[j] for j in c_state]
	all_scores.append(fun(c_score))
all_scores.sort()
mid = int((len(all_scores)-1)/2)
print(all_scores[mid])
	
