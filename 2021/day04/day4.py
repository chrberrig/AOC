from aocd import get_data
import numpy as np
from itertools import permutations

f = get_data(day=4)
f = f.split("\n\n")
calls, *plates_raw = f
calls = [int(c) for c in calls.split(",")]
plates = [np.array([[int(x.strip()) for x in list(filter(None, pline.split(" ")))] for pline in p.split("\n")]) for p in plates_raw]
#print(calls)
plates_tmp = list(np.copy(plates))
[print(i, p) for i, p in enumerate(plates)]
check_ax = lambda plate: np.any([np.all(line==-1) for line in plate])
def play(calls_list, plates_list):
	for c in calls_list:
		for i, p in enumerate(plates_list):
			p[np.where(p==c)] = -1
			if check_ax(p) or check_ax(p.T):
				coords = list(zip(*np.where(p!=-1)))
				unmarked = [p[i] for i in coords]
				score = c*np.sum(unmarked)
				return score
				
print(play(calls, plates_tmp))

			
def play_last(calls_list, plates_list):
	for c in calls_list:
		if len(plates_list)==1:
			p = plates_list[0]
			p[np.where(p==c)] = -1
			if (check_ax(p) or check_ax(p.T)):
				coords = list(zip(*np.where(p!=-1)))
				unmarked = [p[i] for i in coords]
				score = c*np.sum(unmarked)
				return score
		else:
			survive = []
			for p in plates_list:
				p[np.where(p==c)] = -1
				if not (check_ax(p) or check_ax(p.T)):
					survive.append(p)
			plates_list = survive
		
print(play_last(calls, plates_tmp))
