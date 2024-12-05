from .types import Rule, PageUpdate, to_rule, to_update

if __name__ == "__main__":
    rules: list[Rule] = []
    updates: list[PageUpdate] = []
    valid_updates: list[PageUpdate] = []

    with open("./day5/input") as file:
        lines = [line.strip() for line in file.readlines()]

    for line in lines:
        if "|" in line:
            rule = to_rule(line)
            rules.append(rule)
        elif "," in line:
            update = to_update(line)
            updates.append(update)

    PageUpdate.set_rules(rules)

    for update in updates:
        if update.is_valid():
            valid_updates.append(update)

    print(sum(update.middle() for update in valid_updates))
