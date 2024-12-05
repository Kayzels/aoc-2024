from .types import Rule, PageUpdate, to_rule, to_update

if __name__ == "__main__":
    rules: list[Rule] = []
    updates: list[PageUpdate] = []
    invalid_updates: list[PageUpdate] = []

    with open("./day5/input") as file:
        lines = [line.strip() for line in file.readlines()]

    for line in lines:
        if "|" in line:
            rule = to_rule(line)
            rules.append(rule)
        elif "," in line:
            update = to_update(line, rules)
            updates.append(update)

    for update in updates:
        if not update.is_valid():
            invalid_updates.append(update)

    for update in invalid_updates:
        update.fix()

    print(sum(update.middle() for update in invalid_updates))
