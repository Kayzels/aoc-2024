from enum import Enum
from typing import NamedTuple, Final


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class Position(NamedTuple):
    row: int
    col: int


class Board:
    orig: tuple[str, ...]

    @classmethod
    def set_orig(cls, lines: list[str]) -> None:
        cls.orig = tuple(lines)

    def __init__(self, lines: list[str]):
        self._val: list[list[str]] = [[y for y in x] for x in lines]
        self._idx: int = 0

    def get(self, pos: Position) -> str | None:
        if not self.is_valid(pos):
            return None
        return self._val[pos.row][pos.col]

    def set(self, pos: Position, val: str) -> None:
        if not self.is_valid(pos):
            return
        self._val[pos.row][pos.col] = val

    def is_valid(self, pos: Position) -> bool:
        return (
            pos.row >= 0
            and pos.col >= 0
            and pos.row < len(self._val)
            and pos.col < len(self._val[0])
        )

    def reset(self) -> None:
        self._val = [[y for y in x] for x in self.orig]
        self._idx = 0

    def __iter__(self) -> "Board":
        self._idx = 0
        return self

    def __next__(self) -> list[str]:
        if self._idx >= len(self._val):
            raise StopIteration
        val = self._val[self._idx]
        self._idx += 1
        return val


class Guard:
    def __init__(self, direction: Direction, position: Position, board: Board):
        self.direction: Direction = direction
        self.position: Position = position
        self.board: Board = board
        self.start_pos: Final[Position] = position
        self.start_dir: Final[Direction] = direction
        self.board.set(self.start_pos, "S")
        self.looping: bool = False

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

    def is_obstacle(self, next_position: Position) -> bool:
        row, col = next_position
        next_loc = self.board.get(next_position)
        if next_loc == "#" or next_loc == "O":
            return True
        return False

    def next_position(self) -> Position | None:
        if self.looping:
            return None
        match self.direction:
            case Direction.UP:
                next_position = Position(self.position.row - 1, self.position.col)
            case Direction.RIGHT:
                next_position = Position(self.position.row, self.position.col + 1)
            case Direction.DOWN:
                next_position = Position(self.position.row + 1, self.position.col)
            case Direction.LEFT:
                next_position = Position(self.position.row, self.position.col - 1)
        if not self.board.is_valid(next_position):
            return None
        if self.is_obstacle(next_position):
            self.turn()
            return self.next_position()
        return next_position

    def write_dir(self, next_position: Position) -> None:
        if not self.board.is_valid(next_position) or self.looping:
            return
        board_loc = self.board.get(next_position)
        if board_loc is None:
            return
        match self.direction:
            case Direction.UP:
                if "U" in board_loc:
                    self.looping = True
                    return
                self.board.set(next_position, board_loc + "U")
                # self.board.set(next_position, self.board.get(next_position) + "U")
            case Direction.RIGHT:
                if "R" in board_loc:
                    self.looping = True
                    return
                self.board.set(next_position, board_loc + "R")
            case Direction.DOWN:
                if "D" in board_loc:
                    self.looping = True
                    return
                self.board.set(next_position, board_loc + "D")
            case Direction.LEFT:
                if "L" in board_loc:
                    self.looping = True
                    return
                self.board.set(next_position, board_loc + "L")

    def travel(self, position: Position | None) -> None:
        if not self.looping and position is not None and self.board.is_valid(position):
            self.write_dir(position)
            self.position = position

    def count(self) -> int:
        acc = 0
        for line in self.board:
            for word in line:
                counted = False
                for letter in ("S", "U", "R", "D", "L"):
                    if letter in word and not counted:
                        acc += 1
                        counted = True
        return acc

    def go(self) -> None:
        next_position = self.next_position()
        while next_position is not None:
            self.travel(next_position)
            next_position = self.next_position()

    def add_obstacle(self, row: int, col: int) -> None:
        self.board.set(Position(row, col), "O")

    def reset(self) -> None:
        self.direction = self.start_dir
        self.position = self.start_pos
        self.looping = False
        self.board.reset()


def get_start(board: Board) -> tuple[Direction, Position]:
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
