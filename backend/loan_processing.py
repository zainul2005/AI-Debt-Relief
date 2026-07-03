class Loan:
    def __init__(self, loan_id, lender_name, loan_type,
                 outstanding_amount, overdue_months):

        self.loan_id = loan_id
        self.lender_name = lender_name
        self.loan_type = loan_type
        self.outstanding_amount = outstanding_amount
        self.overdue_months = overdue_months


def calculate_settlement(loan):

    settlement = 50

    if loan.overdue_months > 6:
        settlement += 15
    elif loan.overdue_months > 3:
        settlement += 10
    elif loan.overdue_months > 0:
        settlement += 5

    settlement = min(settlement,75)

    return settlement


def loan_priority(loan):

    if loan.overdue_months >= 6:
        return "High"

    elif loan.overdue_months >= 3:
        return "Medium"

    return "Low"


def negotiation_letter(loan):

    return f"""
Dear {loan.lender_name},

I am currently facing financial difficulties and request a settlement for my outstanding loan.

Suggested Settlement: {calculate_settlement(loan)}%

Thank you for your understanding.

Regards,
Borrower
"""


loan = Loan(
    101,
    "State Bank of India",
    "Personal Loan",
    500000,
    5
)

print("Loan Processing Report")
print("-"*40)
print("Settlement Percentage:",calculate_settlement(loan),"%")
print("Priority:",loan_priority(loan))
print(negotiation_letter(loan))