
class DonationAmount:
    def __init__(self, amount: float):
        if amount is None:
            raise ValueError("Donation amount cannot be None")
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero")
        self._value = float(amount)

    def __eq__(self, other):
        return isinstance(other, DonationAmount) and self._value == other._value

    def __str__(self):
        return f"{self._value:.2f}"

    def value(self):
        return self._value
