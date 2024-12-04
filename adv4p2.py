import numpy as np
input = open("input.txt", "r", encoding="utf-8").read()
lines = np.array([list(l.strip()) for l in input.split("\n") if l.strip() != ""])

def count_x(a):
    word = "MAS"
    rows, cols = a.shape
    if rows != 3 or cols != 3:
        return 0
    count = 0
    for j in range(-cols + 1, cols):
        for m in [a, np.fliplr(a)]:
            s = "".join(m.diagonal(j))
            count += s.count(word) + s[::-1].count(word)
    return count == 2

count = 0
rows, cols = lines.shape
for i in range(rows):
    for j in range(cols):
        count += count_x(lines[i:i+3,j:j+3])

print(count)
    