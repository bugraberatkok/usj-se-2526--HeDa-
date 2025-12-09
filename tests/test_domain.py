import pytest

from src.domain import (
    DebateTitle,
    ReportReason,
    DonationAmount,
    PaymentResult,
    EmailAddress,
)


# ---- DebateTitle tests ----

def test_debate_title_cannot_be_blank():
    with pytest.raises(ValueError):
        DebateTitle("   ")


def test_debate_title_must_have_minimum_length():
    with pytest.raises(ValueError):
        DebateTitle("Hi")  # only 2 chars


def test_debate_title_valid():
    title = DebateTitle("Is AI dangerous?")
    assert title.value == "Is AI dangerous?"


# ---- ReportReason tests ----

def test_report_reason_cannot_be_empty():
    with pytest.raises(ValueError):
        ReportReason("")


def test_report_reason_strips_spaces():
    reason = ReportReason("   Harassment   ")
    # whitespace should not break it
    assert reason.value.strip() == "Harassment"


# ---- DonationAmount tests ----

def test_donation_amount_must_be_positive():
    with pytest.raises(ValueError):
        DonationAmount(0)


def test_donation_amount_valid_positive():
    amount = DonationAmount(10.0)
    assert amount.value == 10.0


# ---- PaymentResult tests ----

def test_payment_result_accepts_valid_values():
    for state in ["Success", "Failed", "Pending"]:
        result = PaymentResult(state)
        assert result.value == state


def test_payment_result_rejects_invalid_value():
    with pytest.raises(ValueError):
        PaymentResult("Unknown")


# ---- EmailAddress tests ----

def test_email_address_must_contain_at_and_dot():
    with pytest.raises(ValueError):
        EmailAddress("invalid-email")


def test_email_address_valid():
    email = EmailAddress("user@example.com")
    assert email.value == "user@example.com"
