class ReportReason:
    """Value Object - represents why a user was reported (e.g. 'Harassment', 'Spam')."""
    def __init__(self, reason: str):
        if not reason or not reason.strip():
            raise ValueError("Report reason cannot be empty")
        self._value = reason.strip()

    def __eq__(self, other):
        return isinstance(other, ReportReason) and self._value == other._value

    def __str__(self):
        return self._value

    def value(self):
        return self._value
