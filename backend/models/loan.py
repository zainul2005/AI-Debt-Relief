from sqlalchemy import Column, Integer, Float, String
from database import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)

    lender = Column(String)

    loan_type = Column(String)

    outstanding_amount = Column(Float)

    interest_rate = Column(Float)

    emi = Column(Float)

    overdue_months = Column(Integer)

    priority = Column(String)