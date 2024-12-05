input = open("input.txt", "r", encoding="utf-8").read()
p1, p2 = input.split("\n\n")
rules = [l.strip() for l in p1.split("\n") if l.strip() != ""]
updates = [l.strip() for l in p2.split("\n") if l.strip() != ""]

before = {}
after = {}

for rule in rules:
    a, b = [int(v) for v in rule.split("|")]
    if not a in before:
        before[a] = []
    if not b in after:
        after[b] = []
    
    before[a].append(b)
    after[b].append(a)

def valid(p, future, past):
    b = True
    a = True

    if p in before:
        b = all(f in before[p] or (not f in before) for f in future)
    if p in after:
        a = all(f in after[p] or (not f in after) for f in past)
    
    return a and b

sum = 0
for update in updates:
    pages = [int(p) for p in update.split(",")]
    if all(valid(pages[i], pages[i+1:], pages[:i]) for i in range(len(pages))):
        sum += pages[len(pages) // 2]
print(sum)