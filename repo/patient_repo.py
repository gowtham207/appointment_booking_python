from sqlalchemy.orm import Session
from models.patient import Patient


class Patient_Repo:
    def __init__(self, db: Session):
        self.db = db

    def add_patient(self, patient_data):
        self.db.add(patient_data)
        self.db.commit()
        self.db.refresh(patient_data)
        return patient_data.id
