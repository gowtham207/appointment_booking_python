from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from schema.response import ResponseModel
from helper.gender_hanlder import gender_handler
from helper.exception_handler import exception_handler
from repo.patient_repo import Patient_Repo
from models.patient import Patient
from schema.patientSchema import PatientReqModel


class PatientService:
    def __init__(self, db: Session):
        self.patient_repo = Patient_Repo(db)

    @exception_handler
    def add_patient(self, payload: PatientReqModel) -> ResponseModel:
        gender = gender_handler(payload.gender)
        patient_data = Patient(
            full_name=payload.full_name,
            gender=gender,
            phone=payload.phone,
            email=payload.email,
            dob=payload.dob
        )
        user_id = self.patient_repo.add_patient(patient_data)
        return ResponseModel(success=True, message="Patient added successfully", data={"user_id": user_id})
