input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]
pairs = [l.split() for l in lines]
left = sorted([int(s[0]) for s in pairs])
right = sorted([int(s[1]) for s in pairs])
dist = 0
for i in range(len(left)):
    dist += abs(left[i] - right[i])
print(dist)