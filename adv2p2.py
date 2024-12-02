input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]

count = 0

def test_level(levels):
    inc = True
    dec = True
    for i in range(len(levels) - 1):
        if not (1 <= (levels[i + 1] - levels[i]) <= 3):
            inc = False
        if not (1 <= (levels[i] - levels[i + 1]) <= 3):
            dec = False
    return inc or dec

for line in lines:
    levels = [int(l) for l in line.split()]
    removed = []
    for i in range(0, len(levels)):
        r = list(levels)
        r.pop(i)
        removed.append(r)

    if test_level(levels) or sum([test_level(l) for l in removed]) > 0:
        count += 1
print(count)

    
    