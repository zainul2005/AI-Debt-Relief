from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserProfile(BaseModel):
    monthly_income: float
    monthly_expenses: float
    lump_sum: float


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    monthly_income: Optional[float] = None
    monthly_expenses: Optional[float] = None
    lump_sum: Optional[float] = None

    class Config:
        from_attributes = True