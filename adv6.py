import numpy as np
input = open("input.txt", "r", encoding="utf-8").read()
m = np.array([list(l.strip()) for l in input.split("\n") if l.strip() != ""])

directions = [
    np.array([-1, 0]),
    np.array([0, 1]),
    np.array([1, 0]),
    np.array([0, -1]),
]
d = 0

pos = None
for j in range(len(m)):
    for i in range(len(m[0])):
        if m[j][i] == '^':
            m[j][i] = 'X'
            pos = np.array([j, i]) + directions[d]
            break
count = 1

while True:
    if m[*pos] == '#':
        pos -= directions[d]
        d = (d + 1) % len(directions)
    elif m[*pos] == '.':
        m[*pos] = 'X'
        count += 1
    pos += directions[d]

    if pos[0] < 0 or pos[0] >= len(m) or pos[1] < 0 or pos[1] >= len(m[0]):
        break
print(count)