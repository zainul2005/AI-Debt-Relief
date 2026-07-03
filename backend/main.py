from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from models.user import User
from models.loan import Loan
from routers import auth
from routers import profile
from routers import loans
from routers import ai
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="FinRelief AI API",
    description="AI Powered Debt Relief Platform",
    version="1.0.0"
)
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(loans.router)
app.include_router(ai.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5180",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5180"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to FinRelief AI Backend",
        "status": "Running Successfully"
    }


@app.get("/health")
def health():
    return {
        "server": "Running",
        "database": "Connected",
        "api": "Working"
    }


@app.get("/dashboard")
def dashboard():
    return {
        "monthly_income": 60000,
        "monthly_expenses": 25000,
        "monthly_surplus": 35000,
        "total_emi": 18000,
        "debt_ratio": "30%",
        "stress_level": "LOW"
    }


@app.get("/settlement")
def settlement():
    return {
        "prediction": "65%",
        "recommended_amount": "₹3,25,000",
        "estimated_savings": "₹1,75,000"
    }


@app.get("/rights")
def rights():
    return {
        "rights": [
            "Fair treatment by lenders",
            "No harassment during recovery",
            "Right to settlement discussion",
            "Right to written agreement",
            "Confidential financial information"
        ]
    }