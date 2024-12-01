group1: list[int] = []
group2: list[int] = []

with open("./day1/input") as file:
    lines = [line.strip() for line in file.readlines()]

for line in lines:
    val1, val2 = line.split()
    group1.append(int(val1))
    group2.append(int(val2))

group1.sort()
group2.sort()
