from fastapi import APIRouter, Depends
from api.v1 import auth, location, patient
from core.swagger import bearer_scheme

api_router = APIRouter(prefix="")


api_router.include_router(auth.router, tags=['Authentication'])
api_router.include_router(location.router, prefix='/api/v1',
                          tags=['location'], dependencies=[Depends(bearer_scheme)])
api_router.include_router(patient.router, prefix='/api/v1',
                          tags=['patient'])
