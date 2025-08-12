# Application/routes/auth.py

from fastapi import APIRouter
from application.models.user import SignupRequest, LoginRequest

router = APIRouter()

@router.post("/signup")
async def signup(user: SignupRequest):
    return {"message": f"User {user.email} signed up successfully."}

@router.post("/login")
async def login(user: LoginRequest):
    return {"message": f"User {user.email} logged in successfully."}
