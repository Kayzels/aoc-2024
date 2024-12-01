from .data import group1, group2

differences: list[int] = []
for i in range(len(group1)):
    differences.append(abs(group1[i] - group2[i]))

print(sum(differences))
