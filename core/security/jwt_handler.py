from jose import jwt
from datetime import datetime, timedelta
from config import ALGORITHM


def decode_token(secret: str, value: str):
    try:
        payload = jwt.decode(value, secret, algorithms=[ALGORITHM])
        return payload
    except Exception as err:
        print("Error while decode the payload in server")
        raise err


def encode_token(
    data: dict,
    secret: str,
    expires_delta: timedelta,
    token_type: str
) -> str:
    try:
        to_encode = data.copy()

        now = datetime.utcnow()
        expire = now + expires_delta

        to_encode.update({
            "iat": now,
            "exp": expire,
            "type": token_type
        })

        return jwt.encode(to_encode, secret, algorithm=ALGORITHM)
    except Exception as err:
        print("Error while encode the secret")
        raise err
