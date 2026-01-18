from fastapi import APIRouter, Depends, status
from schema.user import userSignup, userLogin, userMFAEnable, MfaValidatorReq
from schema.response import ResponseModel
from api.deps import get_db
from sqlalchemy.orm import Session
from service.auth_service import AuthService
from starlette.middleware.base import BaseHTTPMiddleware

router = APIRouter(prefix="/auth")


@router.post("/signup", response_model=ResponseModel, status_code=status.HTTP_201_CREATED, summary="User Signup", description="""API is used to register a new user in the system by collecting essential details such as 
            full name, email, password, role, and gender.The email must be unique. Upon successful registration, the user account is created 
            "and ready for authentication.""")
def signup(payload: userSignup, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    return auth_service.register_user(payload)


@router.post("/login", response_model=ResponseModel, status_code=status.HTTP_200_OK, summary='User Login', description="""API is used to authenticate an existing user using their registered email and password.
                On successful authentication, the system returns an access token and user details 
                to allow secure access to protected resources.""")
def login(payload: userLogin, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    return auth_service.login_user(payload)


@router.post("/enable-mfa", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def enable_mfa(payload: userMFAEnable, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    return auth_service.enable_mfa(payload)


@router.post("/verify-mfa", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def check_mfa(payload: MfaValidatorReq, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    return auth_service.verify_mfa(payload)
