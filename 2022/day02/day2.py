from aocd import get_data
import numpy as np

f = get_data(day=2)
f = [tuple(single_round.split(" ")) for single_round in f.split("\n")]

char_range = lambda start_char, stop_char, step=1: [chr(x) for x in range(ord(start_char), ord(stop_char), step)]

translate_tup1 = lambda t: (ord(t[0])-ord("A")+1, ord(t[1])-ord("X")+1)
translate_tup2 = lambda t: (ord(t[0])-ord("A")+1, (ord(t[0])-ord("A") + (ord(t[1])-ord("X")-1))%3 + 1)

f_trans1 = [translate_tup1(p) for p in f]
f_trans2 = [translate_tup2(p) for p in f]

tmp = lambda p1, p2: (1+p2-p1)%3
rps_int = lambda *p: (2-tmp(*p), tmp(*p)) 
"""
determine winner of rock-paper-sissors
input int: 0 rock, 1 paper, 2, scissors
output tuple: (2, 0) p1 wins, (0, 2) p2 wins, (1, 1) draw
this is the branch-less approach
""" 

temps = [tmp(*p) for p in f_trans1]
winnings = [rps_int(*p) for p in f_trans1]
partials = [(rps_int(*p)[1]*3, p[1]) for p in f_trans1]
points = [rps_int(*p)[1]*3 + p[1] for p in f_trans1]

[print(k) for k in zip(f, f_trans1, temps, winnings, partials, points)]

res1 = sum(points)
print(res1)

temps2 = [tmp(*p) for p in f_trans2]
winnings2 = [rps_int(*p) for p in f_trans2]
partials2 = [(rps_int(*p)[1]*3, p[1]) for p in f_trans2]
points2 = [rps_int(*p)[1]*3 + p[1] for p in f_trans2]

[print(k) for k in zip(f, f_trans2, temps2, winnings2, partials2, points2)]

res2 = sum(points2)
print(res2)


