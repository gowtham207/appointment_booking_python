from pyotp import TOTP
import pyotp


def generate_totp_secret() -> str:
    return pyotp.random_base32(40)


def generate_otp_uri(secret: str, username: str, issuer_name: str) -> str:
    totp = pyotp.TOTP(secret)
    return totp.provisioning_uri(name=username, issuer_name=issuer_name)


def verify_mfa(secret: str, otp_code: str) -> bool:
    totp = pyotp.TOTP(secret)
    return totp.verify(otp_code)
