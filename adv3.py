import re

input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]
expr = "".join(lines)

print(sum([int(a) * int(b) for a,b in re.findall(r'mul\(([\d]{1,3}),([\d]{1,3})\)', expr)]))

    
    