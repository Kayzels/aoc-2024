from .guard import Guard, get_start, Board


def get_search(board: Board) -> Guard:
    guard = Guard(start[0], start[1], board)
    guard.go()
    return guard


def count_new_obs(search_board: Board) -> int:
    guard = Guard(start[0], start[1], orig_board)
    total = 0
    for row, line in enumerate(search_board):
        print(row, end=" ", flush=True)
        for col, word in enumerate(line):
            if "U" in word or "R" in word or "D" in word or "L" in word:
                guard.reset()
                guard.add_obstacle(row, col)
                guard.go()
                if guard.looping:
                    total += 1
    print()
    return total


if __name__ == "__main__":
    with open("./day6/input") as file:
        lines = [line.strip() for line in file.readlines()]

    Board.set_orig(lines)
    orig_board = Board(lines)
    board = Board(lines)
    start = get_start(board)
    first_search = get_search(board).board

    print(count_new_obs(first_search))
