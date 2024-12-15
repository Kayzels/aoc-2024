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


def move(
    positions: list[Position], last_ind: int, last_val: int
) -> tuple[list[Position], int, int]:
    pos = positions[last_ind]
    if pos.value < 0 or pos.count <= 0 or pos.value > last_val:
        return positions, last_ind - 1, last_val

    last_val = pos.value

    # get first right sized blank
    first_ind = 0
    first_pos = positions[first_ind]

    while first_pos.value >= 0 or (first_pos.value < 0 and first_pos.count < pos.count):
        first_ind += 1
        if first_ind >= last_ind:
            return positions, last_ind - 1, last_val
        first_pos = positions[first_ind]

    positions[first_ind].value = pos.value
    positions[last_ind].value = -1

    if first_pos.count > pos.count:
        diff = first_pos.count - pos.count
        positions[first_ind].count = pos.count
        positions.insert(first_ind + 1, Position(-1, diff))
        return positions, last_ind, last_val

    return positions, last_ind - 1, last_val


def convert(positions: list[Position]) -> list[Position]:
    # get first non-blank from right
    last_ind = len(positions) - 1
    last_pos = positions[last_ind]
    while last_pos.count <= 0 or last_pos.value < 0:
        last_ind -= 1
        last_pos = positions[last_ind]
    last_val = last_pos.value

    while last_ind > 0:
        positions, last_ind, last_val = move(positions, last_ind, last_val)

    return positions


def calculate(positions: list[Position]) -> int:
    index: int = 0
    acc: int = 0
    for position in positions:
        if position.value < 0:
            index += int(position.count)
            continue
        for i in range(int(position.count)):
            acc += int(position.value) * (index + i)
        index += int(position.count)
    return acc


def to_string(positions: list[Position]) -> str:
    result: str = ""
    for pos in positions:
        val = pos.value
        if val < 0:
            val = "."
        else:
            val = str(val)
        for i in range(pos.count):
            result += val
    return result


with open("./day9/input") as file:
    info = file.readline().strip()

positions = convert(to_positions(info))
print(calculate(positions))
