from fastapi import APIRouter, Depends, status
from schema.response import ResponseModel
from api.deps import get_db
from sqlalchemy.orm import Session
from schema.patientSchema import PatientReqModel
from service.patient_service import PatientService
router = APIRouter()


@router.post("/patients", response_model=ResponseModel, status_code=status.HTTP_201_CREATED)
def add_patient(payload: PatientReqModel, db: Session = Depends(get_db)):
    service = PatientService(db)
    return service.add_patient(payload)
