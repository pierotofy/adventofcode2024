import numpy as np
input = open("input.txt", "r", encoding="utf-8").read()
m = np.array([[int(n) if n != '.' else -1 for n in l.strip()] for l in input.split("\n") if l.strip() != ""])
ths = []
height, width = m.shape
directions = [
    np.array([-1, 0]),
    np.array([0, 1]),
    np.array([1, 0]),
    np.array([0, -1]),
]

for j in range(height):
    for i in range(width):
        if m[j][i] == 0:
            ths.append(np.array([j, i]))

def count_th(th):
    def check(p, target):
        if p[0] < 0 or p[0] >= height or p[1] < 0 or p[1] >= width:
            return 0

        if m[*p] == 9 and target == 9:
            return 1
        elif m[*p] == target:
            c = 0
            for d in directions:
                c += check(p + d, target + 1)
            return c
        else:
            return 0

    return check(th, 0)

count = 0
for th in ths:
    count += count_th(th)
print(count)
        


