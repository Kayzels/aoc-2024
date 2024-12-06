from .guard import Guard, get_start, Board

if __name__ == "__main__":
    with open("./day6/input") as file:
        lines = [line.strip() for line in file.readlines()]

    board = Board(lines)
    start = get_start(board)
    guard = Guard(start[0], start[1], board)
    guard.go()
    print(guard.count())
