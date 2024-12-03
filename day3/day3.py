import re

with open("./day3/input") as file:
    data = file.read()

filter_pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))|."

data = re.sub(filter_pattern, lambda m: m.group(1) or "", data)
data = data.replace("\n", "")


def mult_matches(data: str) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total = 0
    matches: list[tuple[str, str]] = re.findall(pattern, data)
    for match in matches:
        total += int(match[0]) * int(match[1])
    return total


# Part 1
print(f"Part 1: {mult_matches(data)}")

# Part 2
neg_pattern = r"(don't\(\).*?(?:do\(\)|$))"
data = re.sub(neg_pattern, "", data)

print(f"Part 2: {mult_matches(data)}")
