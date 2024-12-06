from enum import Enum
from typing import NamedTuple


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class Position(NamedTuple):
    row: int
    col: int


class Guard:
    def __init__(
        self, direction: Direction, position: Position, board: list[list[str]]
    ):
        self.direction: Direction = direction
        self.position: Position = position
        self.board: list[list[str]] = board

    def turn(self) -> None:
        match self.direction:
            case Direction.UP:
                self.direction = Direction.RIGHT
            case Direction.RIGHT:
                self.direction = Direction.DOWN
            case Direction.DOWN:
                self.direction = Direction.LEFT
            case Direction.LEFT:
                self.direction = Direction.UP

    def on_board(self, position: Position) -> bool:
        return (
            position.row >= 0
            and position.col >= 0
            and position.row < len(self.board)
            and position.col < len(self.board[0])
        )

    def is_obstacle(self, next_position: Position) -> bool:
        row, col = next_position
        if self.board[row][col] == "#":
            return True
        return False

    def next_position(self) -> Position | None:
        match self.direction:
            case Direction.UP:
                next_position = Position(self.position.row - 1, self.position.col)
            case Direction.RIGHT:
                next_position = Position(self.position.row, self.position.col + 1)
            case Direction.DOWN:
                next_position = Position(self.position.row + 1, self.position.col)
            case Direction.LEFT:
                next_position = Position(self.position.row, self.position.col - 1)
        if not self.on_board(next_position):
            return None
        if self.is_obstacle(next_position):
            self.turn()
            return self.next_position()
        return next_position

    def travel(self, position: Position | None) -> None:
        self.board[self.position.row][self.position.col] = "X"
        if position is not None and self.on_board(position):
            self.position = position

    def count(self) -> int:
        acc = 0
        for line in self.board:
            acc += line.count("X")
        return acc


def get_start(board: list[list[str]]) -> tuple[Direction, Position]:
    for row, line in enumerate(board):
        match line:
            case line if "^" in line:
                direction = Direction.UP
                position = Position(row, line.index("^"))
                return (direction, position)
            case line if ">" in line:
                direction = Direction.RIGHT
                position = Position(row, line.index(">"))
                return (direction, position)
            case line if "v" in line:
                direction = Direction.DOWN
                position = Position(row, line.index("v"))
                return (direction, position)
            case line if "<" in line:
                direction = Direction.LEFT
                position = Position(row, line.index("<"))
                return (direction, position)
            case _:
                pass
    raise Exception("Couldn't find start")
