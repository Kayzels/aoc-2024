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


def get_m(x_point: Point) -> list[Point]:
    points: list[Point] = []
    possible_points: list[Point] = [
        Point(x_point.row - 1, x_point.col - 1),
        Point(x_point.row - 1, x_point.col),
        Point(x_point.row - 1, x_point.col + 1),
        Point(row=x_point.row, col=x_point.col - 1),
        Point(row=x_point.row, col=x_point.col + 1),
        Point(row=x_point.row + 1, col=x_point.col - 1),
        Point(row=x_point.row + 1, col=x_point.col),
        Point(row=x_point.row + 1, col=x_point.col + 1),
    ]
    for point in possible_points:
        if valid_point(point):
            if lines[point.row][point.col] == "M":
                points.append(point)
    return points


def next_dir(start: Point, second: Point, search: str) -> Point | None:
    direction: Point = Point(second.row - start.row, second.col - start.col)

    next = Point(second.row + direction.row, second.col + direction.col)
    if valid_point(next):
        return next if lines[next.row][next.col] == search else None
    return None


total = 0
for row_index, line in enumerate(lines):
    for col_index, char in enumerate(line):
        if char == "X":
            x_point = Point(row_index, col_index)
            m_points = get_m(x_point)
            for m_point in m_points:
                a_point = next_dir(x_point, m_point, "A")
                if a_point is not None:
                    s_point = next_dir(m_point, a_point, "S")
                    if s_point is not None:
                        total += 1

print(total)
