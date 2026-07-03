from pydantic import BaseModel
from typing import Optional


class LoanCreate(BaseModel):
    lender: str
    loan_type: str
    outstanding_amount: float
    interest_rate: float
    emi: float
    overdue_months: int
    priority: str


class LoanResponse(BaseModel):
    id: int
    lender: str
    loan_type: str
    outstanding_amount: float
    interest_rate: float
    emi: float
    overdue_months: int
    priority: str

    class Config:
        from_attributes = True