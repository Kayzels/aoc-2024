# Single file with builtins, done after other way

# Counter used for part 2
from collections import Counter

with open("./day1/input") as file:
    lines = [line.strip().split() for line in file.readlines()]

group1, group2 = (list(map(int, x)) for x in map(sorted, zip(*lines)))

# Part 1
print(f"Part 1: {sum([abs(x - y) for x, y in zip(group1, group2)])}")

# Part 2
count = Counter(group2)
print(f"Part 2: {sum([num * count[num] for num in group1])}")
