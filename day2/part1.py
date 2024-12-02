with open("./day2/input") as file:
    lines = [
        list(map(int, x)) for x in [line.strip().split() for line in file.readlines()]
    ]


def is_safe(a: list[int]) -> bool:
    increasing = all(a[i] < a[i + 1] for i in range(len(a) - 1))
    decreasing = all(a[i] > a[i + 1] for i in range(len(a) - 1))
    diff_three = all(abs(a[i] - a[i + 1]) <= 3 for i in range(len(a) - 1))
    return (increasing or decreasing) and diff_three


lines = list(filter(is_safe, lines))
print(len(lines))
