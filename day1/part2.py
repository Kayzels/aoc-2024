from .data import group1, group2

similarities: list[int] = []

for num1 in group1:
    count = 0
    for num2 in group2:
        if num1 == num2:
            count += 1
    similarities.append(num1 * count)

print(sum(similarities))
