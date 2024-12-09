input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]

line = [int(ch) for ch in lines[0]]
disk = []
idx = 0
space_map = []
for i in range(0, len(line), 2):
    block = line[i]
    disk += [str(idx)] * block

    if i + 1 < len(line):
        space = line[i + 1]
        if space > 0:
            space_map.append((len(disk), len(disk) + space))
            disk += ["."] * space
    idx += 1

free_idx = 0
block_idx_start = len(disk) - 1

while block_idx_start >= 0:
    cur_block = ""
    block_idx_end = -1

    while block_idx_start >= 0:
        if cur_block == "" and disk[block_idx_start].isnumeric():
            cur_block = disk[block_idx_start]
            block_idx_end = block_idx_start + 1
        elif cur_block != "" and disk[block_idx_start] != cur_block:
            block_idx_start += 1
            break
        
        block_idx_start -= 1

    block_len = block_idx_end - block_idx_start
    for i in range(len(space_map)):
        s, e = space_map[i]
        if e - s >= block_len and block_idx_start > s:
            disk[s:s+block_len] = disk[block_idx_start:block_idx_end]
            disk[block_idx_start:block_idx_end] = "." * block_len
            space_map[i] = (s+block_len, e)
            break

    block_idx_start -= 1

sum = 0
for i, block in enumerate(disk):
    if block == '.':
        continue
    sum += int(block) * i
print(sum)
     