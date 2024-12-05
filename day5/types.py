from typing import NamedTuple


class Rule(NamedTuple):
    first: int
    second: int


def to_rule(line: str) -> Rule:
    vals = [int(val) for val in line.split("|")]
    return Rule(*vals)


class PageUpdate:
    rules: list[Rule] = []

    def __init__(self, order: list[int]) -> None:
        self.order: list[int] = order

    @classmethod
    def set_rules(cls, rules: list[Rule]) -> None:
        cls.rules = rules

    def _check_rule(self, rule: Rule) -> bool:
        if rule.first not in self.order or rule.second not in self.order:
            return True
        return self.order.index(rule.first) < self.order.index(rule.second)

    def middle(self) -> int:
        index = len(self.order) // 2
        return self.order[index]

    def is_valid(self) -> bool:
        return all(self._check_rule(rule) for rule in self.rules)

    def fix(self) -> None:
        if not self.is_valid():
            for rule in self.rules:
                if not self._check_rule(rule):
                    copied_order = self.order.copy()
                    copied_order.remove(rule.first)
                    index = copied_order.index(rule.second)
                    copied_order.insert(index, rule.first)
                    self.order = copied_order
                    self.fix()


def to_update(line: str) -> PageUpdate:
    vals = [int(val) for val in line.split(",")]
    return PageUpdate(vals)
