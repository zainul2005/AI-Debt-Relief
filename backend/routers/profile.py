from fastapi import APIRouter

router = APIRouter(
    prefix="/profile",
    tags=["Financial Profile"]
)


@router.get("/")
def get_profile():

    return {

        "monthly_income": 60000,

        "monthly_expenses": 25000,

        "monthly_surplus": 35000,

        "lump_sum": 100000,

        "debt_ratio": "30%",

        "financial_health": "Healthy"

    }


@router.put("/update")
def update_profile():

    return {

        "message": "Financial profile updated successfully"

    }