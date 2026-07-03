class User:
    def __init__(self, monthly_income, monthly_expenses):
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses


class Loan:
    def __init__(self, loan_id, lender_name, outstanding_amount, interest_rate, emi, overdue_months):
        self.loan_id = loan_id
        self.lender_name = lender_name
        self.outstanding_amount = outstanding_amount
        self.interest_rate = interest_rate
        self.emi = emi
        self.overdue_months = overdue_months


def calculate_financial_health(user, loans):
    total_emi = sum(loan.emi for loan in loans)
    total_outstanding = sum(loan.outstanding_amount for loan in loans)

    surplus = user.monthly_income - user.monthly_expenses - total_emi

    if user.monthly_income > 0:
        emi_ratio = (total_emi / user.monthly_income) * 100
        debt_to_income = (total_outstanding / user.monthly_income) * 100
    else:
        emi_ratio = 0
        debt_to_income = 0

    if emi_ratio > 50:
        stress_level = "High"
    elif emi_ratio >= 30:
        stress_level = "Medium"
    else:
        stress_level = "Low"

    return {
        "Total EMI": total_emi,
        "Outstanding Amount": total_outstanding,
        "Monthly Surplus": surplus,
        "EMI Ratio (%)": round(emi_ratio,2),
        "Debt To Income (%)": round(debt_to_income,2),
        "Stress Level": stress_level
    }


user = User(60000,25000)

loans = [
    Loan(1,"SBI",500000,10,12000,0),
    Loan(2,"HDFC",200000,12,6000,2)
]

result = calculate_financial_health(user,loans)

print(result)