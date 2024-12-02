input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]

count = 0
for line in lines:
    levels = [int(l) for l in line.split()]
    inc = True
    dec = True
    for i in range(len(levels) - 1):
        if not (1 <= (levels[i + 1] - levels[i]) <= 3):
            inc = False
        if not (1 <= (levels[i] - levels[i + 1]) <= 3):
            dec = False
    if inc or dec:
        count += 1
print(count)

    
    