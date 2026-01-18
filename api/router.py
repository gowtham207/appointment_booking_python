from fastapi import APIRouter
from api.v1 import auth, location

api_router = APIRouter()


api_router.include_router(auth.router, prefix='/v1', tags=['Authentication'])
# api_router.include_router()
