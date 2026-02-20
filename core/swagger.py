from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends

bearer_scheme = HTTPBearer()


def swagger_auth(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
):
    return credentials
