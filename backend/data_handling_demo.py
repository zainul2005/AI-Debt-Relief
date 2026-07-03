from database import engine, SessionLocal, Base
from models import User

# Create database tables
Base.metadata.create_all(bind=engine)

db = SessionLocal()

user = User(
    email="zain@example.com",
    password="password123",
    monthly_income=60000,
    monthly_expenses=25000
)

db.add(user)
db.commit()

users = db.query(User).all()

print("Stored Users")
print("-" * 30)

for u in users:
    print(
        f"ID: {u.id}, "
        f"Email: {u.email}, "
        f"Income: {u.monthly_income}, "
        f"Expenses: {u.monthly_expenses}"
    )

db.close()