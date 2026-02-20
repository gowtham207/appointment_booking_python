from config import *
from core.security.jwt_handler import *
from core.security.mfa_handler import *
from core.security.token_generator import *
from core.security.bcrypt_handler import *


def generate_auth_session(user_id: str) -> dict:
    return {
        "auth_session": generate_auth_session_token({
            'user_id': user_id
        })
    }


def generate_user_token(user_id: str) -> dict:
    access_token = generate_access_token({'user_id': str(user_id)})
    refresh_token = generate_refresh_token({'user_id': str(user_id)})
    id_token = generate_id_token({'user_id': str(user_id)})
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "id_token": id_token,
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }
