from pydantic import BaseModel, EmailStr
from models.enum import UserRole


class userSignup(BaseModel):
    full_name: str
    email: EmailStr
    phone: str | None = None
    password: str
    role: UserRole
    gender: str


class userLogin(BaseModel):
    email: EmailStr
    password: str


class userLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: str
    id_token: str


class userMFAEnable(BaseModel):
    user_id: str


class MfaValidatorReq(BaseModel):
    auth_session: str
    mfa_code: str
