from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

from .domain import ReportReason, DebateTitle


app = FastAPI()


# ---- Pydantic schemas (for HTTP layer) ----

class DebateResponse(BaseModel):
    id: int
    title: str
    participants: int


class ReportRequest(BaseModel):
    reportedUserId: int = Field(gt=0)
    reason: str = Field(min_length=1)


class ReportResponse(BaseModel):
    message: str
    reportedUserId: int
    reason: str


# ---- In-memory fake data (no real DB yet) ----

_FAKE_DEBATES = [
    {"id": 1, "title": "Is AI dangerous?", "participants": 12},
    {"id": 2, "title": "Should university be free?", "participants": 7},
]


# ---- Basic health endpoint ----

@app.get("/health")
def health():
    return {"status": "ok"}


# ---- Critical endpoint 1: browse debates ----

@app.get("/debates", response_model=List[DebateResponse])
def list_debates():
    """
    Allows users to browse debates.
    Uses simple in-memory data for now.
    """
    # Domain layer: validate titles using DebateTitle value object
    validated = []
    for d in _FAKE_DEBATES:
        title_vo = DebateTitle(d["title"])
        validated.append(
            {
                "id": d["id"],
                "title": title_vo.value,
                "participants": d["participants"],
            }
        )
    return validated


# ---- Critical endpoint 2: report inappropriate behaviour ----

@app.post("/reports", response_model=ReportResponse)
def create_report(report: ReportRequest):
    """
    Allows a user to report inappropriate behaviour.
    Enforces 'Categorize report' invariant:
    - User cannot report without specifying the category/reason.
    """
    # Domain layer: validate reason using ReportReason value object
    reason_vo = ReportReason(report.reason)

    # Normalde burada DB'ye kayıt vs. olur.
    # Şimdilik sadece bir onay mesajı döndürüyoruz.
    return ReportResponse(
        message="Report received",
        reportedUserId=report.reportedUserId,
        reason=reason_vo.value,
    )


# Not: FastAPI genelde uvicorn ile çalıştırılır:
# uvicorn src.app:app --reload
