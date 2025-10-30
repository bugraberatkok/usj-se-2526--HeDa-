from value_objects import ModerationReason
from entities import User


class Report:
    def __init__(self, report_id: str, reporter: User, reported: User, reason: ModerationReason):
        if not report_id or report_id.strip() == "":
            raise ValueError("Report must have a unique ID")
        self._id = report_id
        self._reporter = reporter
        self._reported = reported
        self._reason = reason

    def get_id(self) -> str:
        return self._id

    def get_reporter(self) -> User:
        return self._reporter

    def get_reported(self) -> User:
        return self._reported

    def get_reason(self) -> ModerationReason:
        return self._reason

    def __eq__(self, other):
        return isinstance(other, Report) and self._id == other._id
