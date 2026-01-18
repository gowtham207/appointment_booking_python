from sqlalchemy.orm import Session
from schema.user import userSignup, userMFAEnable, userLogin, MfaValidatorReq
from models.user import User
from core.security import *
from repo.user_repo import userRepo
from fastapi.responses import JSONResponse
from schema.response import ResponseModel
from helper.gender_hanlder import gender_handler
from helper.exception_handler import exception_handler


class AuthService:
    def __init__(self, db_connection: Session):
        self.user_repo = userRepo(db_connection)

    @exception_handler
    def register_user(self, user_data: userSignup) -> ResponseModel:
        check_user = self.user_repo.get_user_by_email(user_data.email)
        if check_user:
            return JSONResponse(status_code=400, content={"message": "User already exists"})
        hashed_password = generate_password_hash(user_data.password)
        new_user = User(
            email=user_data.email,
            password_hash=hashed_password,
            full_name=user_data.full_name,
            role=user_data.role,
            phone=user_data.phone,
            gender=gender_handler(user_data.gender)
        )
        created_user = self.user_repo.add_user(new_user)
        return ResponseModel(message="User created successfully", data={"user_id": created_user.id}, status=True)

    @exception_handler
    def login_user(self, login_data: userLogin) -> ResponseModel:
        user = self.user_repo.get_user_by_email(login_data.email)
        # Check the user in thr database
        if user is None:
            return JSONResponse(status_code=404, content={"message": "User not found"})
        # Compare the password and password hash

        is_password_valid = compare_passwords(
            login_data.password, user.password_hash)

        if not is_password_valid:
            return JSONResponse(status_code=401, content={"message": "Invalid credentials"})

        # Check the user is active or not
        if not user.is_active:
            return JSONResponse(status_code=403, content={"message": "User account is inactive"})

        # If MFA is enabled, generate an auth session token
        if user.mfa_enabled and user.mfa_hash:
            auth_session_token = generate_auth_session_token(user.id)
            return ResponseModel(message="MFA required", data=auth_session_token, status=True)

        self.user_repo.update_last_login(user)
        return ResponseModel(message="Login successful", data=generate_user_token(user.id), status=True)

    @exception_handler
    def enable_mfa(self, login_data: userMFAEnable) -> ResponseModel:
        user: User = self.user_repo.get_user_by_id(login_data.user_id)
        # console.log()
        print(f"MFA of user {user.email} was {user.mfa_enabled}")
        if user is None:
            return JSONResponse(status_code=404, content={"message": "User not found"})

        if user.mfa_enabled:
            return JSONResponse(status_code=400, content={"message": "MFA is already enabled for this user"})

        mfa_hash = generate_totp_secret()
        mfa_uri = generate_otp_uri(
            mfa_hash, user.email, "AppointmentApp")

        user.mfa_hash = mfa_hash
        user.mfa_enabled = True

        self.user_repo.update_user(user)

        data = {
            "mfa_uri": mfa_uri,
            "auth_session": generate_auth_session(user.id)
        }
        return ResponseModel(message="MFA enabled successfully", data=data, status=True)

    @exception_handler
    def verify_mfa(self, payload: MfaValidatorReq) -> ResponseModel:
        user: User = self.user_repo.get_user_by_id(payload.user_id)

        if user is None:
            return JSONResponse(status_code=404, content={"message": "User not found"})

        if not user.mfa_enabled:
            return JSONResponse(status_code=400, content={"message": "MFA is was not enabled for this user"})

        verification = verify_mfa(user.mfa_hash, payload.mfa_code)
        if not verification:
            return JSONResponse(status_code=400, content={"message": "incorrect MFA"})

        return ResponseModel(message="Login successful", data=return_token(user.id), status=True)
