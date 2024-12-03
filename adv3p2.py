import re

input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]
expr = "".join(lines)

matches = re.findall(r'(mul|do|don\'t)\(([\d]*),?([\d]*)\)', expr)
sum = 0
enabled = True
for op, a, b in matches:
    if enabled and op == 'mul' and a != '' and b != '':
        sum += int(a) * int(b)
    elif op == 'do':
        enabled = True
    elif op == 'don\'t':
        enabled = False
print(sum)
    