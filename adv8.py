import numpy as np
from itertools import combinations
input = open("input.txt", "r", encoding="utf-8").read()

m = np.array([list(l.strip()) for l in input.split("\n") if l.strip() != ""])
antennas = {}
for j in range(len(m)):
    for i in range(len(m[0])):
        c = str(m[j][i])
        if c.isdigit() or c.isalpha():
            if not c in antennas:
                antennas[c] = []
            antennas[c].append(np.array([j, i]))

out = np.zeros_like(m, dtype=np.bool)

for a in antennas:
    for p1,p2 in combinations(antennas[a], 2):
        v = p2 - p1
        x1 = p1 - v
        x2 = p2 + v
        if x1[0] >= 0 and x1[0] < len(out) and x1[1] >= 0 and x1[1] < len(out[0]):
            out[tuple(x1)] = True
        if x2[0] >= 0 and x2[0] < len(out) and x2[1] >= 0 and x2[1] < len(out[0]):
            out[tuple(x2)] = True

print(np.count_nonzero(out))