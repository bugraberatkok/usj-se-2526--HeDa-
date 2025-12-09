from dataclasses import dataclass


# ---- Value Objects ----

@dataclass(frozen=True)
class DebateTitle:
    value: str

    def __post_init__(self):
        text = (self.value or "").strip()
        if len(text) == 0:
            raise ValueError("DebateTitle cannot be blank")
        if len(text) < 3:
            raise ValueError("DebateTitle must have at least 3 characters")


@dataclass(frozen=True)
class ReportReason:
    value: str

    def __post_init__(self):
        text = (self.value or "").strip()
        if len(text) == 0:
            raise ValueError("ReportReason cannot be empty")


@dataclass(frozen=True)
class DonationAmount:
    value: float

    def __post_init__(self):
        if self.value <= 0:
            raise ValueError("DonationAmount must be greater than zero")


@dataclass(frozen=True)
class PaymentResult:
    value: str

    def __post_init__(self):
        allowed = {"Success", "Failed", "Pending"}
        if self.value not in allowed:
            raise ValueError(f"PaymentResult must be one of {allowed}")


@dataclass(frozen=True)
class EmailAddress:
    value: str

    def __post_init__(self):
        text = (self.value or "").strip()
        if "@" not in text or "." not in text:
            raise ValueError("EmailAddress must contain '@' and '.'")
