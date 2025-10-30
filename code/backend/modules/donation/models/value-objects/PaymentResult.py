class PaymentResult:
    VALID_RESULTS = {"success", "failed", "pending"}

    def __init__(self, result: str):
        if not result or not result.strip():
            raise ValueError("Payment result cannot be empty")
        normalized = result.strip().lower()
        if normalized not in self.VALID_RESULTS:
            raise ValueError(f"Invalid payment result: '{result}'. Must be one of {self.VALID_RESULTS}")
        self._value = normalized

    def __eq__(self, other):
        return isinstance(other, PaymentResult) and self._value == other._value

    def __str__(self):
        return self._value.capitalize()

    def value(self):
        return self._value
