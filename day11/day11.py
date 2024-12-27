def update_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        val = str(stone)
        return [int(val[: len(val) // 2]), int(val[len(val) // 2 :])]
    else:
        return [stone * 2024]


def blink(arrangement: dict[int, int]) -> dict[int, int]:
    new_arrangement: dict[int, int] = {}
    for stone in arrangement:
        new_stones = update_stone(stone)
        for new_stone in new_stones:
            if new_stone not in new_arrangement:
                new_arrangement[new_stone] = 0
            new_arrangement[new_stone] += arrangement[stone]
    return new_arrangement


if __name__ == "__main__":
    with open("./day11/input") as file:
        arrangement = {i: 1 for i in map(int, file.readline().strip().split())}

    PART_1_REPS = 25
    PART_2_REPS = 75

    part1_count = 0
    for i in range(PART_2_REPS):
        arrangement = blink(arrangement)
        if i == PART_1_REPS - 1:
            part1_count = sum(arrangement.values())

    print(f"Part 1: {part1_count}")
    print(f"Part 2: {sum(arrangement.values())}")
