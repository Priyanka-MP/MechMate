from fastapi import APIRouter
from Application.models.user import SignupRequest, LoginRequest

router = APIRouter()

@router.post("/signup")
def signup(user: SignupRequest):
    return {"message": "User registered successfully", "user": user}

@router.post("/login")
def login(credentials: LoginRequest):
    return {"message": "Login successful", "user": credentials.email}
