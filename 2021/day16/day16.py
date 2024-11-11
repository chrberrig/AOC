from aocd import get_data
import numpy as np
from itertools import permutations

f = get_data(day=14)
f = f.split("\n\n")
polymer, rules = f
rules = [tuple(r.split(" -> ")) for r in rules.split("\n")]
insert = lambda rule: "".join([rule[0][0], rule[1], rule[0][1]])
rdict = {r[0]: insert(r) for r in rules}
print(rdict)
print(polymer)
pairs = ["".join(p) for p in zip(polymer[:-1], polymer[1:])]
pdict = {p: pairs.count(p) for p in pairs}

def polymerazation(polymer, steps=10):
	print(steps)
	if steps==0:
		return polymer
	else:
		out_polymer = []
		for i, e in enumerate(polymer[:-1]):
			p = polymer[i:i+2]
			if p in rdict:
				out_polymer.append(rdict[p][:-1])
		out_polymer.append(polymer[-1])		
		out_polymer = str("".join(out_polymer))
		return polymerazation(out_polymer, steps=steps-1)

print("--"*20)
res_polymer = polymerazation(polymer, steps=10)

cdict = {x: res_polymer.count(x) for x in set(list(l for l in res_polymer))}
print(cdict)
print(max(cdict.values()) - min(cdict.values()))
	
#pt2:
def pair_count(pairs_dict, steps=10):
	print(steps)
	if steps==0:
		return pairs_dict
	else:
		pdict = {}
		for p, c in pairs_dict.items():
			if p in rdict:
				pdict[p] = pairs_dict[p] - c
				for x in [rdict[p][:2], rdict[p][1:]]:
					if x in pairs_dict:
						pdict[x] = c + pairs_dict[x]
					else:
						pdict[x] = c
		print(pdict)
		return pair_count(pdict, steps=steps-1)

def med(pdict):
	edict = {x: 0 for x in list(set(list("".join(pdict.keys()))))}
	for k, v in pdict.items():
		for x in k:
			edict[x] += pdict[k]
	#print(edict)
	#for x in edict:
	#	if x not in [polymer[0], polymer[-1]]:
	#		edict[x] = edict[x]/2
	#	else:
	#		edict[x] = (edict[x]+1)/2

	return edict
print(polymer)
print(pdict)

pdict = pair_count(pdict, steps=10)
print("#"*20)
print(pdict)
print("#"*20)
edict = med(pdict)
print(max(edict.values()) - min(edict.values()))
print(edict)
