from dataclasses import dataclass


@dataclass
class Position:
    value: int
    count: int


def to_positions(info: str) -> list[Position]:
    current_val = 0
    positions: list[Position] = []
    for index, char in enumerate(info):
        cnt = int(char)
        if index % 2 == 1:
            positions.append(Position(-1, cnt))
        else:
            positions.append(Position(current_val, cnt))
            current_val += 1
    return positions


def convert(positions: list[Position]) -> list[Position]:
    first_ind: int = 0
    last_ind: int = len(positions) - 1

    while first_ind < last_ind:
        first_pos = positions[first_ind]
        while first_pos.value >= 0:
            first_ind += 1
            first_pos = positions[first_ind]
        # After this, first is the first blank

        last_pos = positions[last_ind]
        while last_pos.count <= 0 or last_pos.value < 0:
            last_ind -= 1
            last_pos = positions[last_ind]
        # After this, last is the last non blank

        if first_ind >= last_ind:
            break

        if first_pos.count <= last_pos.count:
            positions[first_ind].value = last_pos.value
            positions[last_ind].count = last_pos.count - first_pos.count
        else:
            update_last = Position(last_pos.value, last_pos.count - first_pos.count)
            positions[first_ind] = last_pos
            positions[last_ind] = update_last
            positions.insert(
                first_ind + 1, Position(-1, first_pos.count - last_pos.count)
            )

    positions = list(filter(lambda pos: pos.value >= 0 and pos.count > 0, positions))
    return positions


def calculate(positions: list[Position]) -> int:
    index: int = 0
    acc: int = 0
    for position in positions:
        if position.value < 0:
            continue
        for i in range(int(position.count)):
            acc += int(position.value) * (index + i)
        index += int(position.count)
    return acc


with open("./day9/test_input") as file:
    info = file.readline().strip()

positions = convert(to_positions(info))
print(calculate(positions))
