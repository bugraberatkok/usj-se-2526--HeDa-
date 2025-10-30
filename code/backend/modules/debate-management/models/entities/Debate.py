from enum import Enum
from typing import List
from value_objects import TopicTitle, Timestamp
from entities import User


class DebateStatus(Enum):
    EMPTY = "EMPTY"
    ONGOING = "ONGOING"
    CLOSED = "CLOSED"


class Debate:
    def __init__(self, debate_id: str, topic: TopicTitle, creator: User, created_at: Timestamp):
        if not debate_id or debate_id.strip() == "":
            raise ValueError("Debate must have a non-empty unique ID")
        if not isinstance(topic, TopicTitle):
            raise TypeError("Debate topic must be a TopicTitle value object")
        if not isinstance(created_at, Timestamp):
            raise TypeError("Created_at must be a Timestamp value object")

        self._id = debate_id
        self._topic = topic
        self._creator = creator
        self._participants: List[User] = [creator]
        self._status = DebateStatus.EMPTY
        self._created_at = created_at

    def add_participant(self, user: User):
        if self._status == DebateStatus.CLOSED:
            raise ValueError("Cannot join a closed debate.")
        if user in self._participants:
            raise ValueError("User is already part of this debate.")
        self._participants.append(user)
        self._update_status()

    def remove_participant(self, user: User):
        if user not in self._participants:
            raise ValueError("User is not part of this debate.")
        if user == self._creator:
            raise ValueError("Creator cannot be removed from the debate.")
        self._participants.remove(user)
        self._update_status()

    def close(self):
        if self._status == DebateStatus.CLOSED:
            raise ValueError("Debate is already closed.")
        self._status = DebateStatus.CLOSED

    def _update_status(self):
        if len(self._participants) == 1:
            self._status = DebateStatus.EMPTY
        else:
            self._status = DebateStatus.ONGOING

    def get_id(self) -> str:
        return self._id

    def get_status(self) -> DebateStatus:
        return self._status

    def get_topic(self) -> TopicTitle:
        return self._topic

    def get_participants(self) -> List[User]:
        return self._participants

    def __eq__(self, other):
        if not isinstance(other, Debate):
            return False
        return self._id == other._id
