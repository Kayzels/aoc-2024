class Position(complex):
    def next(self) -> set["Position"]:
        return {
            Position(self.real - 1, self.imag),
            Position(self.real, self.imag + 1),
            Position(self.real + 1, self.imag),
            Position(self.real, self.imag - 1),
        }


class Board:
    def __init__(self, values: list[list[int]]) -> None:
        self._values: list[list[int]] = values
        self.rows: int = len(self._values)
        self.cols: int = len(self._values[0])

    def get(self, pos: Position) -> int:
        return self._values[int(pos.real)][int(pos.imag)]

    def is_valid(self, pos: Position) -> bool:
        return (
            pos.real >= 0
            and pos.imag >= 0
            and pos.real < self.rows
            and pos.imag < self.cols
        )


def go(
    pos: Position,
    value: int = 0,
    finals: set[Position] | None = None,
    route: set[Position] | None = None,
    routes: list[set[Position]] | None = None,
) -> tuple[int, int]:
    if finals is None:
        finals = set()
    if route is None:
        route = {pos}
    if routes is None:
        routes = []

    if value == 9:
        if pos not in finals:
            finals.add(pos)
        routes.append(route)
        return len(finals), len(routes)
    next_positions = filter(lambda p: board.is_valid(p), pos.next())
    for position in next_positions:
        next_val = board.get(position)
        if next_val == value + 1:
            route.add(pos)
            go(position, value + 1, finals, route, routes)
    return len(finals), len(routes)


if __name__ == "__main__":
    with open("./day10/input") as file:
        vals = [
            list(map(int, c))
            for c in [x for x in [line.strip() for line in file.readlines()]]
        ]

    board = Board(vals)

    scores = 0
    ratings = 0
    for i in range(board.rows):
        for j in range(board.cols):
            position = Position(i, j)
            if board.get(position) == 0:
                score, rating = go(position)
                scores += score
                ratings += rating

    print(f"Part 1: {scores}")
    print(f"Part 2: {ratings}")
