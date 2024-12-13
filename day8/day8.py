def on_grid(num: complex, size: complex) -> bool:
    return (
        num.real >= 0
        and num.real < size.real
        and num.imag >= 0
        and num.imag < size.imag
    )


def get_nodes(
    num: complex, others: set[complex], grid_size: complex, repeat: bool = False
) -> set[complex]:
    result: set[complex] = set()
    for other in others:
        if other == num:
            continue
        diff = num - other
        new_num = num + diff
        if not repeat and on_grid(new_num, grid_size):
            result.add(new_num)
            continue
        while on_grid(new_num, grid_size):
            result.add(new_num)
            new_num = new_num + diff
    return result


if __name__ == "__main__":
    with open("./day8/input") as file:
        lines = [line.strip() for line in file.readlines()]

    antennae: dict[str, set[complex]] = {}
    antinodes1: set[complex] = set()
    antinodes2: set[complex] = set()

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != ".":
                if char not in antennae:
                    antennae[char] = set()
                antennae[char].add(complex(row, col))

    for antenna in antennae.values():
        for num in antenna:
            antinodes2.add(num)
            nodes1 = get_nodes(num, antenna, complex(len(lines), len(lines[0])))
            nodes2 = get_nodes(
                num, antenna, complex(len(lines), len(lines[0])), repeat=True
            )
            antinodes1.update(nodes1)
            antinodes2.update(nodes2)

    print(f"Part 1: {len(antinodes1)}")
    print(f"Part 2: {len(antinodes2)}")
