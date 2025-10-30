from enum import Enum
from typing import Optional
from value_objects import MoneyAmount, EmailAddress, Username  # hypothetical imports


class ModeratorStatus(Enum):
    WORKING = "WORKING"
    PAID = "PAID"
    ON_BREAK = "ON_BREAK"


class Moderator:
    """
    Entity: Moderator
    Justification:
        - Has a unique identifier (moderator_id)
        - Exhibits a lifecycle: WORKING → PAID → ON_BREAK → WORKING
        - Maintains mutable state (payment status, workload, etc.)
    """

    def __init__(self, moderator_id: str, username: Username, email: EmailAddress):
        if not moderator_id or moderator_id.strip() == "":
            raise ValueError("Moderator must have a non-empty unique ID")
        if not isinstance(username, Username):
            raise TypeError("Username must be a Value Object of type Username")
        if not isinstance(email, EmailAddress):
            raise TypeError("Email must be a Value Object of type EmailAddress")

        self._id = moderator_id
        self._username = username
        self._email = email
        self._status = ModeratorStatus.WORKING
        self._last_payment: Optional[MoneyAmount] = None

    # --- Behaviours ---

    def mark_as_paid(self, amount: MoneyAmount):
        """
        Transition: WORKING → PAID
        Invariant: can only mark as paid when currently WORKING.
        """
        if self._status != ModeratorStatus.WORKING:
            raise ValueError("Moderator must be WORKING to be marked as PAID.")
        if not isinstance(amount, MoneyAmount):
            raise TypeError("Payment must be a MoneyAmount value object.")

        self._last_payment = amount
        self._status = ModeratorStatus.PAID

    def go_on_break(self):
        """
        Transition: PAID → ON_BREAK
        Invariant: can only go on break after being PAID.
        """
        if self._status != ModeratorStatus.PAID:
            raise ValueError("Moderator can only go on break after payment.")
        self._status = ModeratorStatus.ON_BREAK

    def resume_work(self):
        """
        Transition: ON_BREAK → WORKING
        Invariant: can only resume work from ON_BREAK state.
        """
        if self._status != ModeratorStatus.ON_BREAK:
            raise ValueError("Moderator must be ON_BREAK to resume work.")
        self._status = ModeratorStatus.WORKING

    # --- Accessors ---

    def get_id(self) -> str:
        return self._id

    def get_status(self) -> ModeratorStatus:
        return self._status

    def get_last_payment(self) -> Optional[MoneyAmount]:
        return self._last_payment

    def get_username(self) -> Username:
        return self._username

    # --- Equality (based on identity only) ---

    def __eq__(self, other):
        if not isinstance(other, Moderator):
            return False
        return self._id == other._id
