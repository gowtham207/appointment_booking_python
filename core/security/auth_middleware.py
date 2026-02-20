from fastapi import Request, status
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from config import SECRET_KEY, ID_SECRET_KEY
from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, req: Request, call_next):
        print(f"AuthMiddleware: Processing request for {req.url.path}")
        if req.url.path.lower() in ["/docs", "/redoc", "/openapi.json", "/health", '/api/v1/patients'] or req.url.path.startswith("/auth"):
            print("AuthMiddleware: Skipping authentication for public endpoint")
            return await call_next(req)

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
        return await call_next(req)


class PostAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, req: Request, call_next):
        print(f"AuthMiddleware: Processing request for {req.url.path}")

        if req.url.path.lower() in ["/docs", "/redoc", "/openapi.json", "/health", '/api/v1/patients'] or req.url.path.startswith("/auth"):
            print("AuthMiddleware: Skipping authentication for public endpoint")
            return await call_next(req)

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
        return await call_next(req)
