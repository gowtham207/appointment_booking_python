from fastapi import APIRouter
from api.v1 import auth, location

api_router = APIRouter(prefix="")


api_router.include_router(auth.router, prefix='/', tags=['Authentication'])
api_router.include_router(location.router, prefix='/api/v1', tags=['location'])
