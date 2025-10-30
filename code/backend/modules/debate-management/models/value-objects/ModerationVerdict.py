class ModerationVerdict:
    def __init__(self, verdict: str):
        if not verdict or not verdict.strip():
            raise ValueError("Moderation verdict cannot be empty")
        self._value = verdict.strip()

    def __eq__(self, other):
        return isinstance(other, ModerationVerdict) and self._value == other._value

    def __str__(self):
        return self._value

    def value(self):
        return self._value
