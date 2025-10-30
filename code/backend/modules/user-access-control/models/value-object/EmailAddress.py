import re

class EmailAddress:
    def __init__(self, value: str):
        if not value:
            raise ValueError("Email cannot be empty")
        value = value.strip().lower()
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
            raise ValueError("Invalid email format")
        self._value = value

    def __eq__(self, other):
        return isinstance(other, EmailAddress) and self._value == other._value

    def __str__(self):
        return self._value

    def value(self):
        return self._value
