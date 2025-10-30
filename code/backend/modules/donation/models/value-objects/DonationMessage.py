class DonationMessage:
    def __init__(self, message: str):
        if message is None:
            raise ValueError("Donation message cannot be None")
        self._value = message.strip()
        # Empty message is allowed, but trimmed

    def __eq__(self, other):
        return isinstance(other, DonationMessage) and self._value == other._value

    def __str__(self):
        return self._value

    def value(self):
        return self._value
