import numpy as np
input = open("input.txt", "r", encoding="utf-8").read()
m = np.array([list(l.strip()) for l in input.split("\n") if l.strip() != ""])

directions = [
    np.array([-1, 0]),
    np.array([0, 1]),
    np.array([1, 0]),
    np.array([0, -1]),
]

def has_loop(m):
    d = 0

    pos = None
    for j in range(len(m)):
        for i in range(len(m[0])):
            if m[j][i] == '^':
                m[j][i] = 'X'
                pos = np.array([j, i]) + directions[d]
                break
    check = np.zeros((len(m), len(m[0])))

    while True:
        if m[*pos] == '#':
            if not check[*pos]:
                check[*pos] = d
            elif check[*pos] == d:
                return True

            pos -= directions[d]
            d = (d + 1) % len(directions)
        elif m[*pos] == '.':
            m[*pos] = 'X'
        pos += directions[d]

        if pos[0] < 0 or pos[0] >= len(m) or pos[1] < 0 or pos[1] >= len(m[0]):
            break
    
    return False

count = 0

for j in range(len(m)):
    for i in range(len(m[0])):
        if m[j, i] == '^' or m[j,i] == '#':
            continue

        mc = m.copy()
        mc[j, i] = '#'
        if has_loop(mc):
            count += 1
            print(count, i, j)
print(count)