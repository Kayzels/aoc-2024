from .guard import Guard, get_start, Board
import copy


def get_first_search() -> Board:
    new_board = copy.deepcopy(board)
    guard = Guard(start[0], start[1], new_board)
    while True:
        next_position = guard.next_position()
        guard.travel(next_position)
        if next_position is None:
            break
    return guard.board


def search_loop(board: Board) -> bool:
    guard = Guard(start[0], start[1], board)
    while True:
        next_position = guard.next_position()
        guard.travel(next_position)
        if next_position is None:
            break
    return guard.looping


def count_new_obs(orig_board: Board, search_board: Board) -> int:
    total = 0
    for row, line in enumerate(search_board):
        print(row, end=" ", flush=True)
        for col, word in enumerate(line):
            if "U" in word or "R" in word or "D" in word or "L" in word:
                new_board = copy.deepcopy(orig_board)
                new_board[row][col] = "#"
                if search_loop(new_board):
                    total += 1
    print()
    return total


if __name__ == "__main__":
    with open("./day6/input") as file:
        board: Board = [
            [y for y in x] for x in [line.strip() for line in file.readlines()]
        ]

    start = get_start(board)
    orig_board: Board = copy.deepcopy(board)
    first_search = get_first_search()

    print(count_new_obs(orig_board, first_search))
