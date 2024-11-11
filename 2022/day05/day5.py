from aocd import get_data
import copy
import numpy as np

f = get_data(day=5)
state, inst = f.split("\n\n")

# inst = inst.split("\n")
parse_inst_line = lambda line: [int(w) for i, w in enumerate(line.split(" ")) if i%2==1]
inst = [parse_inst_line(l) for l in inst.split("\n")] 

# can probably be done more elegant!
state = np.array([list(l) for l in state.split("\n")])
state = np.array(list(filter(lambda k: k[-1]!=" ", state.T)))
state = [list(np.flip(l)) for l in state.T[:-1].T]
rm_all = lambda lst, target: [c for c in lst if c != target]
state_init = [rm_all(l, " ") for l in state]
# [print(s) for s in state_init]

def movecrates(num, fr, to, state, moveall=False):
    crates = []
    s = copy.deepcopy(state)
    for n in range(num):
        c = s[fr - 1].pop(-1)
        crates.append(c)
    if moveall:
        crates.reverse() # determines model 9000 or 9001
    s[to - 1] += crates # more elegant
    return s

def all_moves(instructions, state, **kwargs):
    if instructions == []:
        return state
    else:
        ins, ins_rest = instructions[0], instructions[1:]
        return all_moves(ins_rest, movecrates(*ins, state, **kwargs), **kwargs)

print("--"*20)
# movecrates(3, 2, 5, state)
[print(s) for s in state_init]

print("--"*20)
# should be done w recursive call for functional approach?
# state = state_init.copy()
# for line in inst:
#     state = movecrates(*line, state, moveall=False)
out_state = all_moves(inst, state_init)
print("".join([s[-1] for s in out_state]))

# print("--"*20)
# state = state_init.copy()
# for line in inst:
#     state = movecrates(*line, state, moveall=True)
out_state = all_moves(inst, state_init, moveall=True)
print("".join([s[-1] for s in out_state]))



