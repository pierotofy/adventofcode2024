from itertools import product
from functools import reduce
from operator import add, mul

input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]

concat = lambda x,y: int(str(x) + str(y))
ops = [add,mul,concat]

count = 0
for line in lines:
    value, nums = line.split(":")
    value = int(value)
    nums = [int(n) for n in nums.strip().split(" ")]

    for p in product(ops, repeat=len(nums) - 1):
        n = nums[0]
        for i in range(1, len(nums)):
            n = p[i - 1](n, nums[i])
        if value == n:
            count += value
            break
print(count)
