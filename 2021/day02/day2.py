from aocd import get_data
import numpy as np

f = get_data(day=2)
f = f.split("\n")
h, v = 0, 0
# for i in f:
# 	w, n = i.split(" ")
# 	n = int(n)
# 	if w=="up":
# 		v -= n
# 	elif w=="down":
# 		v += n
# 	elif w=="forward":
# 		h += n
# 	#print(i)
# 	#print(h, v)
# 
# print(h*v)
aim, h, v = 0, 0, 0
for i in f:
	w, n = i.split(" ")
	n = int(n)
	if w=="up":
		aim -= n
	elif w=="down":
		aim += n
	elif w=="forward":
		h += n
		v += aim*n
	#print(i)
	#print(h, v)

print(h*v)
