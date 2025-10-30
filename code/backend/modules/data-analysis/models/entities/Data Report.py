from enum import Enum


class DataReportStatus(Enum):
    FETCHING = "FETCHING"
    SENT_TO_ANALYST = "SENT_TO_ANALYST"


class DataReport:
    def __init__(self, report_id: str):
        if not report_id or report_id.strip() == "":
            raise ValueError("DataReport must have a unique ID")
        self._id = report_id
        self._status = DataReportStatus.FETCHING

    def send_to_analyst(self):
        if self._status != DataReportStatus.FETCHING:
            raise ValueError("Only fetching reports can be sent")
        self._status = DataReportStatus.SENT_TO_ANALYST

    def get_id(self) -> str:
        return self._id

    def get_status(self) -> DataReportStatus:
        return self._status

    def __eq__(self, other):
        return isinstance(other, DataReport) and self._id == other._id
