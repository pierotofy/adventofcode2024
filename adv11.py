input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]
stones = [int(n) for n in lines[0].split(" ")]

for _ in range(25):
    new_stones = [] 
    for i in range(len(stones)):
        s = str(stones[i])
        mid = int(len(s) / 2)
        if stones[i] == 0:
            new_stones.append(1)
        elif len(s) % 2 == 0:
            new_stones.append(int(s[:mid]))
            new_stones.append(int(s[mid:]))
        else:
            new_stones.append(stones[i] * 2024)
        
    stones = new_stones

print(len(stones))
        

