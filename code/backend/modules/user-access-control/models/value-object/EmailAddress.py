import re


class EmailAddress:
    """
    Value Object: EmailAddress
    Bounded Context: User & Access Control

    Represents a validated, normalized email address.
    Equality is based purely on the value of the email string.
    """

    EMAIL_REGEX = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )

    __slots__ = ("__value",)

    def __init__(self, value: str):
        if value is None:
            raise ValueError("Email address cannot be null")

        normalized = value.strip().lower()

        if not normalized:
            raise ValueError("Email address cannot be empty")

        if not self.EMAIL_REGEX.match(normalized):
            raise ValueError(f"Invalid email address format: '{value}'")

        self.__value = normalized

    @property
    def value(self) -> str:
        """Returns the normalized email address."""
        return self.__value

    def equals(self, other: "EmailAddress") -> bool:
        """Compares two EmailAddress objects by value."""
        if not isinstance(other, EmailAddress):
            return False
        return self.__value == other.__value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EmailAddress):
            return False
        return self.__value == other.__value

    def __hash__(self) -> int:
        """Ensures value objects can be used in sets or as dict keys."""
        return hash(self.__value)

    def __str__(self) -> str:
        return self.__value

    def __repr__(self) -> str:
        return f"EmailAddress(value='{self.__value}')"
