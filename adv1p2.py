input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]
pairs = [l.split() for l in lines]
left = sorted([int(s[0]) for s in pairs])
right = sorted([int(s[1]) for s in pairs])
d = {}
sim = 0
for r in right:
    if not r in d:
        d[r] = 1
    else:
        d[r] += 1
for l in left:
    sim += l * d.get(l, 0)
print(sim)
