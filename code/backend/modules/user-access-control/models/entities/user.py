from enum import Enum
from typing import Optional
from value_objects import EmailAddress, Username, ReputationScore  # hypothetical imports


class UserStatus(Enum):
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"


class User:
    """
    Entity: User
    Justification:
        - Has a unique identity (`user_id`)
        - Exhibits a lifecycle (ACTIVE → BANNED → ACTIVE)
        - Mutable state: can be banned/unbanned, reputation can change
    """

    def __init__(self, user_id: str, username: Username, email: EmailAddress):
        if not user_id or user_id.strip() == "":
            raise ValueError("User must have a non-empty unique ID")
        if not isinstance(username, Username):
            raise TypeError("Username must be a Value Object of type Username")
        if not isinstance(email, EmailAddress):
            raise TypeError("Email must be a Value Object of type EmailAddress")

        self._id = user_id
        self._username = username
        self._email = email
        self._status = UserStatus.ACTIVE
        self._reputation = ReputationScore(0)
        self._ban_reason: Optional[str] = None

    # --- Behaviours ---

    def ban(self, reason: str):
        """
        Transition: ACTIVE → BANNED
        Invariant: cannot ban an already banned user
        """
        if self._status == UserStatus.BANNED:
            raise ValueError("User is already banned")
        self._status = UserStatus.BANNED
        self._ban_reason = reason

    def unban(self):
        """
        Transition: BANNED → ACTIVE
        Invariant: can only unban a currently banned user
        """
        if self._status != UserStatus.BANNED:
            raise ValueError("User must be banned before being unbanned")
        self._status = UserStatus.ACTIVE
        self._ban_reason = None

    def update_reputation(self, delta: int):
        """
        Behaviour: adjust reputation score based on interactions
        """
        new_score = self._reputation.value + delta
        self._reputation = ReputationScore(new_score)

    # --- Accessors ---

    def get_id(self) -> str:
        return self._id

    def get_status(self) -> UserStatus:
        return self._status

    def get_reputation(self) -> ReputationScore:
        return self._reputation

    def get_username(self) -> Username:
        return self._username

    def __eq__(self, other):
        """
        Entity equality is based on ID, not value.
        """
        if not isinstance(other, User):
            return False
        return self._id == other._id
