# N = 9
# drawing_lines = 8
# with open('5.txt') as fim:
#     parts = fim.read()[:-1].split("\n\n")
#     drawing = parts[0].split("\n")
#     print(drawing)
#     stacks = [[] for _ in range(N)]
#     for i in range(drawing_lines):
#         line = drawing[i]
#         crates = line[1::4]
#         for s in range(len(crates)):
#             if crates[s] != " ":
#                 stacks[s].append(crates[s])
# stacks = [stack[::-1] for stack in stacks]
# print(stacks)
# for line in parts[1].split("\n"):
#     print(line)
#     tokens = line.split(" ")
#     n, src, dst = map(int, [tokens[1],tokens[3],tokens[5]])
#     src -= 1
#     dst -= 1
#     stacks[dst].extend(stacks[src][-n:])
# tops = [stack[-1] for stack in stacks]
# print("".join(tops))
import re, copy
with open('5.txt','r') as file:
    stack_txt, instruction_data = file.read().split('\n\n')
    stack_txt = stack_txt.split('\n')
    instruction_data = instruction_data.split('\n')
stack_last = stack_txt.pop()
stack = {}
loc = {}
ordering = []
for ii in range(len(stack_last)):
    if stack_last[ii] != '':
        stack[stack_last[ii]] = []
        loc[stack_last[ii]] = ii
        ordering.append(stack_last[ii])
for line in reversed(stack_txt):
    for key in loc.keys():
        if line[loc[key]] != ' ':
            stack[key].append(line[loc[key]])
            
stack2 = copy.deepcopy(stack)

for line in instruction_data:
    if 'move' in line:
        inst_values = re.findall(r'(\d+)', line)
        count = int(inst_values[0])
        ff = inst_values[1]
        tt = inst_values[2]
        for ii in range(count):
            pop_val = stack[ff].pop()
            stack[tt].append(pop_val)
        stack2[tt] += stack2[ff][-count:]
        stack2[ff] = stack2[ff][:-count]

for ii in ordering:
    print(stack2[ii][-1], end = '')