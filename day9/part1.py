def to_positions(info: str) -> list[complex]:
    current_val = 0
    positions: list[complex] = []
    for index, char in enumerate(info):
        cnt = int(char)
        if index % 2 == 1:
            positions.append(complex(-1, cnt))
        else:
            positions.append(complex(current_val, cnt))
            current_val += 1
    return positions


def convert(positions: list[complex]) -> list[complex]:
    first_ind: int = 0
    last_ind: int = len(positions) - 1

    while first_ind < last_ind:
        first_pos = positions[first_ind]
        while first_pos.real >= 0:
            first_ind += 1
            first_pos = positions[first_ind]
        # After this, first is the first blank

        last_pos = positions[last_ind]
        while last_pos.imag <= 0 or last_pos.real < 0:
            last_ind -= 1
            last_pos = positions[last_ind]
        # After this, last is the last non blank

        if first_ind >= last_ind:
            break

        if first_pos.imag <= last_pos.imag:
            new_val = complex(last_pos.real, first_pos.imag)
            update_last = complex(last_pos.real, last_pos.imag - first_pos.imag)
            positions[first_ind] = new_val
            positions[last_ind] = update_last
        else:
            new_val = complex(last_pos.real, last_pos.imag)
            update_last = complex(last_pos.real, last_pos.imag - first_pos.imag)
            positions[first_ind] = new_val
            positions[last_ind] = update_last
            positions.insert(first_ind + 1, complex(-1, first_pos.imag - last_pos.imag))

    positions = list(filter(lambda pos: pos.real >= 0 and pos.imag > 0, positions))
    return positions


def calculate(positions: list[complex]) -> int:
    index: int = 0
    acc: int = 0
    for position in positions:
        if position.real < 0:
            continue
        for i in range(int(position.imag)):
            acc += int(position.real) * (index + i)
        index += int(position.imag)
    return acc


with open("./day9/input") as file:
    info = file.readline().strip()

positions = convert(to_positions(info))
print(calculate(positions))
