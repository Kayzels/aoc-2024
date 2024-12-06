from .guard import Guard, get_start

if __name__ == "__main__":
    with open("./day6/input") as file:
        board = [[y for y in x] for x in [line.strip() for line in file.readlines()]]

    start = get_start(board)
    guard = Guard(start[0], start[1], board)
    while True:
        next_position = guard.next_position()
        guard.travel(next_position)
        if next_position is None:
            break
    print(guard.count())
