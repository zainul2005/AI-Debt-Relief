from datetime import datetime, timedelta

from fastapi import APIRouter

from jose import jwt

SECRET_KEY = "finrelief-secret"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 120

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


def create_access_token():

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": "borrower",
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


@router.post("/login")
def login():

    token = create_access_token()

    return {
        "message": "Login Successful",
        "access_token": token,
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES
    }