class User:
    def __init__(self, monthly_income):
        self.monthly_income = monthly_income


class Loan:
    def __init__(self, loan_id, lender_name, outstanding_amount,
                 interest_rate, emi, overdue_months):

        self.loan_id = loan_id
        self.lender_name = lender_name
        self.outstanding_amount = outstanding_amount
        self.interest_rate = interest_rate
        self.emi = emi
        self.overdue_months = overdue_months


def settlement_prediction(user, loans):

    total_emi = sum(loan.emi for loan in loans)
    total_outstanding = sum(loan.outstanding_amount for loan in loans)

    emi_ratio = (total_emi / user.monthly_income) * 100
    debt_to_income = (total_outstanding / user.monthly_income) * 100

    results = []

    for loan in loans:

        settlement = 50
        risk_score = 0

        if loan.overdue_months > 0:
            settlement += 5
            risk_score += 20

        if emi_ratio > 50:
            settlement += 5
            risk_score += 15

        if loan.interest_rate > 12:
            settlement += 5
            risk_score += 10

        if debt_to_income > 80:
            settlement += 5
            risk_score += 15

        settlement = max(40, min(75, settlement))

        if risk_score >= 40:
            risk = "High"
        elif risk_score >= 20:
            risk = "Medium"
        else:
            risk = "Low"

        results.append({
            "Loan ID": loan.loan_id,
            "Lender": loan.lender_name,
            "Settlement %": settlement,
            "Risk Score": risk_score,
            "Risk Category": risk
        })

    return results


user = User(60000)

loans = [
    Loan(1, "SBI", 500000, 10, 12000, 0),
    Loan(2, "HDFC", 200000, 13, 6000, 2)
]

result = settlement_prediction(user, loans)

print("Settlement Prediction Report")
print("-" * 40)

for loan in result:
    print(loan)