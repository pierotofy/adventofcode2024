from functools import lru_cache
input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]
stones = [int(n) for n in lines[0].split(" ")]

@lru_cache(maxsize=None)
def count(stone, n):
    if n == 0:
        return 1
    
    if stone == 0:
        return count(1, n - 1)

    s = str(stone)
    mid = int(len(s) / 2)
    
    if len(s) % 2 == 0:
        return count(int(s[:mid]), n - 1) + count(int(s[mid:]), n - 1)
    
    return count(stone * 2024, n - 1)

c = 0
for s in stones:
    c += count(s, 75)
print(c)
        

