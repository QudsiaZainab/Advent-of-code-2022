# import collections as c, itertools, re, functools
# r = r'Valve (\w+) .*=(\d*); .*valves? (.*)'
# V, F, D = set(), dict(), c.defaultdict(lambda: 1000)
# for v, f, us, in re.findall(r, open('16.txt').read()):
#     V.add(v)
#     if f != '0': F[v] = int(f)
#     for u in us.split(', ') : D[u, v] = 1
    
# for k, i, j in itertools.product(V, V, V):
#     D[i, j] = min(D[i, j], D[i, k] + D[k, j])

# @functools.cache
# def search(t, u = 'AA', vs = frozenset(F), e = False):
#     tt = max([F[v] * (t - D[u, v] - 1) + search(t - D[u, v] - 1, v, vs - {v}, e)
#     for v in vs if D[u, v] < t] + [search(26, vs = vs) if e else 0])
#     return tt

# print(str(search(30)))

# from collections import deque

# valves = {}
# tunnels = {}

# for line in open('16.txt'):
#     line = line.strip()
#     valve = line.split()[1]
#     flow = int(line.split(";")[0].split("=")[1])
#     targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
#     valves[valve] = flow
#     tunnels[valve] = targets

# dists = {}
# nonempty = []

# for valve in valves:
#     if valve != "AA" and not valves[valve]:
#         continue
    
#     if valve != "AA":
#         nonempty.append(valve)

#     dists[valve] = {valve: 0, "AA": 0}
#     visited = {valve}
    
#     queue = deque([(0, valve)])
    
#     while queue:
#         distance, position = queue.popleft()
#         for neighbor in tunnels[position]:
#             if neighbor in visited:
#                 continue
#             visited.add(neighbor)
#             if valves[neighbor]:
#                 dists[valve][neighbor] = distance + 1
#             queue.append((distance + 1, neighbor))

#     del dists[valve][valve]
#     if valve != "AA":
#         del dists[valve]["AA"]

# indices = {}

# for index, element in enumerate(nonempty):
#     indices[element] = index

# cache = {}

# def dfs(time, valve, bitmask):
#     if (time, valve, bitmask) in cache:
#         return cache[(time, valve, bitmask)]
    
#     maxval = 0
#     for neighbor in dists[valve]:
#         bit = 1 << indices[neighbor]
#         if bitmask & bit:
#             continue
#         remtime = time - dists[valve][neighbor] - 1
#         if remtime <= 0:
#             continue
#         maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit) + valves[neighbor] * remtime)
        
#     cache[(time, valve, bitmask)] = maxval
#     return maxval

# print(dfs(30, "AA", 0))

from collections import deque

valves = {}
tunnels = {}

for line in open('16.txt'):
    line = line.strip()
    valve = line.split()[1]
    flow = int(line.split(";")[0].split("=")[1])
    targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
    valves[valve] = flow
    tunnels[valve] = targets

dists = {}
nonempty = []

for valve in valves:
    if valve != "AA" and not valves[valve]:
        continue
    
    if valve != "AA":
        nonempty.append(valve)

    dists[valve] = {valve: 0, "AA": 0}
    visited = {valve}
    
    queue = deque([(0, valve)])
    
    while queue:
        distance, position = queue.popleft()
        for neighbor in tunnels[position]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            if valves[neighbor]:
                dists[valve][neighbor] = distance + 1
            queue.append((distance + 1, neighbor))

    del dists[valve][valve]
    if valve != "AA":
        del dists[valve]["AA"]

indices = {}

for index, element in enumerate(nonempty):
    indices[element] = index

cache = {}

def dfs(time, valve, bitmask):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]
    
    maxval = 0
    for neighbor in dists[valve]:
        bit = 1 << indices[neighbor]
        if bitmask & bit:
            continue
        remtime = time - dists[valve][neighbor] - 1
        if remtime <= 0:
            continue
        maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit) + valves[neighbor] * remtime)
        
    cache[(time, valve, bitmask)] = maxval
    return maxval

b = (1 << len(nonempty)) - 1

m = 0

for i in range((b + 1) // 2):
    m = max(m, dfs(26, "AA", i) + dfs(26, "AA", b ^ i))

print(m)