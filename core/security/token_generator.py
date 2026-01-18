from core.security import *
from core.security.jwt_handler import encode_token, decode_token
from config import *


def generate_auth_session_token(data: dict) -> str:
    return encode_token(
        data=data,
        secret=SECRET_KEY,
        expires_delta=timedelta(minutes=AUTH_SESSION),
        token_type="auth_session"
    )


def generate_access_token(data: dict) -> str:
    return encode_token(
        data=data,
        secret=SECRET_KEY,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        token_type="access"
    )


def generate_id_token(data: dict) -> str:
    return encode_token(
        data=data,
        secret=ID_SECRET_KEY,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        token_type="id"
    )


def generate_refresh_token(data: dict) -> str:
    return encode_token(
        data=data,
        secret=SECRET_KEY,
        expires_delta=timedelta(hours=REFRESH_TOKEN_EXPIRE_HOURS),
        token_type="refresh"
    )
