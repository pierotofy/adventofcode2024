import numpy as np
input = open("input.txt", "r", encoding="utf-8").read()
lines = np.array([list(l.strip()) for l in input.split("\n") if l.strip() != ""])
flip = np.fliplr(lines)

rows, cols = lines.shape
count = 0
word = "XMAS"

for row in lines:
    s = ''.join(row)
    count += s.count(word) + s[::-1].count(word)
for j in range(cols):
    s = ''.join(lines[i][j] for i in range(rows))
    count += s.count(word) + s[::-1].count(word)     

for j in range(-cols + 1, cols):
    for m in [lines, flip]:
        s = "".join(m.diagonal(j))
        count += s.count(word) + s[::-1].count(word)

print(count)
    