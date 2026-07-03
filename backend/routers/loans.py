from fastapi import APIRouter

router = APIRouter(
    prefix="/loans",
    tags=["Loans"]
)

loans = [
    {
        "id": 1,
        "lender": "HDFC Bank",
        "loan_type": "Personal Loan",
        "outstanding": 500000,
        "interest": 10,
        "emi": 18000,
        "overdue": 0,
        "priority": "Medium"
    },
    {
        "id": 2,
        "lender": "SBI",
        "loan_type": "Credit Card",
        "outstanding": 120000,
        "interest": 18,
        "emi": 6000,
        "overdue": 2,
        "priority": "High"
    }
]


@router.get("/")
def get_loans():
    return loans


@router.get("/{loan_id}")
def get_loan(loan_id: int):

    for loan in loans:
        if loan["id"] == loan_id:
            return loan

    return {"message": "Loan not found"}


@router.post("/add")
def add_loan():

    try:

        return {
            "message": "Loan added successfully"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail="Unable to add loan"
        )
    

    
@router.put("/update/{loan_id}")
def update_loan(loan_id: int):

    return {
        "message": f"Loan {loan_id} updated successfully"
    }


@router.delete("/delete/{loan_id}")
def delete_loan(loan_id: int):

    return {
        "message": f"Loan {loan_id} deleted successfully"
    }