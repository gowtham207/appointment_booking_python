from fastapi import APIRouter, Depends, status
from schema.user import userSignup, userLogin, userMFAEnable, MfaValidatorReq
from schema.response import ResponseModel
from api.deps import get_db
from sqlalchemy.orm import Session
from service.auth_service import AuthService
from starlette.middleware.base import BaseHTTPMiddleware

router = APIRouter(prefix="")


@router.get()
