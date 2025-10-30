class GoodBehaviorPolicy:
    def __init__(self, rules: str):
        if not rules or not rules.strip():
            raise ValueError("Good behavior policy cannot be empty")
        self._rules = rules.strip()

    def __eq__(self, other):
        return isinstance(other, GoodBehaviorPolicy) and self._rules == other._rules

    def __str__(self):
        return self._rules

    def value(self):
        return self._rules
