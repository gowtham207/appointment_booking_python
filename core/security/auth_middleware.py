from fastapi import requests, status
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from config import SECRET_KEY, ID_SECRET_KEY


class AuthMiddleware:
    async def __call__(self, req: requests, call_next):
        if req.url.path.startswith("/api/v1/") and req.method.upper() in ["GET", "HEAD", "OPTIONS"]:
            auth_header = req.headers.get("Authorization")
            if auth_header is None or not auth_header.startswith("Bearer "):
                return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": "Unauthorized"})
            token = auth_header.split(" ")[1]
            try:
                payload = jwt.decode(
                    token, ID_SECRET_KEY, algorithms=["HS256"])
                req.state.user_id = payload.get("user_id")

            except JWTError:
                return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": "Invalid token"})
            return await call_next(req)


class PostAuthMiddleware:
    async def __call__(self, req: requests, call_next):
        if req.url.path.startswith("/api/v1/") and req.method.upper() in ["POST", "PUT", "DELETE"]:
            auth_header = req.headers.get("Authorization")
            if auth_header is None or not auth_header.startswith("Bearer "):
                return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": "Unauthorized"})
            token = auth_header.split(" ")[1]
            try:
                payload = jwt.decode(
                    token, SECRET_KEY, algorithms=["HS256"])
                req.state.user_id = payload.get("user_id")

            except JWTError:
                return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": "Invalid token"})
            return await call_next(req)
