from value_objects import PaymentReference, MoneyAmount
from entities import Donation


class Donator:
    def __init__(self, payment_info: PaymentReference, donation: Donation, amount: MoneyAmount):
        if not isinstance(payment_info, PaymentReference):
            raise TypeError("Invalid payment information")
        self._payment_info = payment_info
        self._donation = donation
        self._amount = amount

    def get_payment_info(self) -> PaymentReference:
        return self._payment_info

    def get_donation(self) -> Donation:
        return self._donation

    def get_amount(self) -> MoneyAmount:
        return self._amount

    def __eq__(self, other):
        return isinstance(other, Donator) and self._payment_info == other._payment_info
