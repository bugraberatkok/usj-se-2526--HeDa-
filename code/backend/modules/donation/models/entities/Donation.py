from enum import Enum
from value_objects import MoneyAmount, PaymentReference


class DonationStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Donation:
    def __init__(self, transaction_id: str, amount: MoneyAmount, payment_ref: PaymentReference):
        if not transaction_id or transaction_id.strip() == "":
            raise ValueError("Donation must have a unique transaction ID")
        self._id = transaction_id
        self._amount = amount
        self._payment_ref = payment_ref
        self._status = DonationStatus.PENDING

    def mark_completed(self):
        if self._status != DonationStatus.PENDING:
            raise ValueError("Donation cannot be completed twice")
        self._status = DonationStatus.COMPLETED

    def mark_failed(self):
        if self._status == DonationStatus.COMPLETED:
            raise ValueError("Completed donation cannot fail")
        self._status = DonationStatus.FAILED

    def get_id(self) -> str:
        return self._id

    def get_status(self) -> DonationStatus:
        return self._status

    def __eq__(self, other):
        return isinstance(other, Donation) and self._id == other._id
