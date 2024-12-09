def do(
    acc: int, test: int, nums: tuple[int, ...], index: int, concat: bool = False
) -> bool:
    if acc > test:
        return False
    if index >= len(nums):
        return acc == test

    if acc == 0:
        mult_acc = nums[index]
    else:
        mult_acc = acc * nums[index]
    mult_check = do(mult_acc, test, nums, index + 1, concat)
    if mult_check:
        return True

    sum_acc = acc + nums[index]
    sum_check = do(sum_acc, test, nums, index + 1, concat)
    if sum_check:
        return True

    if concat:
        if acc == 0:
            concat_acc = nums[index]
        else:
            concat_acc = int(str(acc) + str(nums[index]))
        concat_check = do(concat_acc, test, nums, index + 1, concat)
        if concat_check:
            return True

    return False


if __name__ == "__main__":
    with open("./day7/input") as file:
        lines = [line.strip() for line in file.readlines()]
    data = [
        (int(x[0]), tuple(int(y) for y in x[1].strip().split()))
        for x in [line.split(":") for line in lines]
    ]

    part1 = 0
    for test, nums in data:
        if do(0, test, nums, 0, concat=False):
            part1 += test
    print(f"Part 1: {part1}")

    part2 = 0
    for test, nums in data:
        if do(0, test, nums, 0, concat=True):
            part2 += test
    print(f"Part 2: {part2}")
