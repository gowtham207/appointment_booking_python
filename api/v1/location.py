from fastapi import APIRouter, Depends, status
from schema.response import ResponseModel
from api.deps import get_db
from sqlalchemy.orm import Session
from service.location_service import LocationService
from schema.locationSchema import LocationModel

router = APIRouter()


@router.post("/location", response_model=ResponseModel, status_code=status.HTTP_201_CREATED)
def add_location(paylaod: LocationModel, db: Session = Depends(get_db)):
    service = LocationService(db)
    return service.add_location(paylaod)


@router.get("/location/{location_id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def get_location_by_id(location_id: str, db: Session = Depends(get_db)):
    service = LocationService(db)
    return service.get_location_by_id(location_id)\



@router.get("/locations", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def get_all_locations(db: Session = Depends(get_db)):
    service = LocationService(db)
    return service.get_all_locations()


@router.delete("/location/{location_id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def delete_location(location_id: str, db: Session = Depends(get_db)):
    service = LocationService(db)
    return service.delete_location(location_id)


@router.put("/location/{location_id}", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def update_location(location_id: str, payload: LocationModel, db: Session = Depends(get_db)):
    service = LocationService(db)
    return service.update_location(location_id, payload)
