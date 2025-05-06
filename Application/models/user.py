from pydantic import BaseModel
from typing import Optional

class SignupRequest(BaseModel):
    name: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

class AssistanceRequest(BaseModel):
    user_id: int
    issue: str
    location: str
    contact_number: Optional[str] = None
