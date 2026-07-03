from fastapi import APIRouter, HTTPException
from utils.ai_helper import call_ai

router = APIRouter(
    prefix="/ai",
    tags=["AI Services"]
)


@router.get("/financial-health")
def financial_health():

    try:

        return {
            "monthly_surplus": 35000,
            "debt_ratio": "30%",
            "stress_level": "LOW",
            "financial_health": "Healthy"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Financial Health Error: {str(e)}"
        )


@router.get("/settlement-predictor")
def settlement_prediction():

    try:

        prompt = """
        Generate a debt settlement recommendation for a borrower
        with moderate financial stress.
        """

        result = call_ai(prompt)

        return {
            "prediction": result,
            "status": "Success"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Settlement Prediction Error: {str(e)}"
        )


@router.get("/negotiation-email")
def negotiation_email():

    try:

        prompt = """
        Generate a professional loan settlement negotiation email.
        """

        result = call_ai(prompt)

        return {
            "email": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Negotiation Email Error: {str(e)}"
        )


@router.get("/borrower-rights")
def borrower_rights():

    try:

        return {
            "rights": [
                "Fair treatment by lenders",
                "No harassment during recovery",
                "Right to written settlement agreement",
                "Access to loan information",
                "Privacy protection"
            ]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Borrower Rights Error: {str(e)}"
        )