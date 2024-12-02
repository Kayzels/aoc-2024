with open("./day2/input") as file:
    lines = [
        list(map(int, x)) for x in [line.strip().split() for line in file.readlines()]
    ]


def is_safe(a: list[int]) -> bool:
    increasing = all(a[i] < a[i + 1] for i in range(len(a) - 1))
    decreasing = all(a[i] > a[i + 1] for i in range(len(a) - 1))
    diff_three = all(abs(a[i] - a[i + 1]) <= 3 for i in range(len(a) - 1))
    return (increasing or decreasing) and diff_three


# Part 1
safe: list[list[int]] = []
unsafe: list[list[int]] = []
for line in lines:
    if is_safe(line):
        safe.append(line)
    else:
        unsafe.append(line)

print(f"Part 1: {len(safe)}")


# Part 2
def dampen_line(a: list[int]) -> bool:
    valid = False
    for i in range(len(a)):
        b = a.copy()
        b.pop(i)
        valid = is_safe(b)
        if valid:
            break
    return valid


dampened = list(filter(dampen_line, unsafe))

print(f"Part 2: {len(safe) + len(dampened)}")
