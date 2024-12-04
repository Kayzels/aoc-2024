from typing import NamedTuple

with open("./day4/input") as file:
    lines = [line.strip() for line in file.readlines()]


class Point(NamedTuple):
    row: int
    col: int


def valid_point(point: Point) -> bool:
    return (
        point.row >= 0
        and point.col >= 0
        and point.row < len(lines)
        and point.col < len(lines[0])
    )


def is_x(a_point: Point) -> bool:
    pairs: list[tuple[Point, Point]] = [
        (
            Point(a_point.row - 1, a_point.col - 1),
            Point(a_point.row + 1, a_point.col + 1),
        ),
        (
            Point(a_point.row - 1, a_point.col + 1),
            Point(a_point.row + 1, a_point.col - 1),
        ),
    ]
    for check_point in pairs:
        for point in check_point:
            if not valid_point(point):
                return False
    valid = True
    for pair in pairs:
        forms_mas = (
            lines[pair[0].row][pair[0].col] == "M"
            and lines[pair[1].row][pair[1].col] == "S"
        ) or (
            lines[pair[0].row][pair[0].col] == "S"
            and lines[pair[1].row][pair[1].col] == "M"
        )
        valid = valid and forms_mas
    return valid


total = 0
for row_index, line in enumerate(lines):
    for col_index, char in enumerate(line):
        if char == "A":
            a_point = Point(row_index, col_index)
            if is_x(a_point):
                total += 1

print(total)
