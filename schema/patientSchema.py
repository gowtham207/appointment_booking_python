from pydantic import BaseModel
from datetime import date


class PatientReqModel(BaseModel):
    full_name: str
    dob: date | None = None
    gender: str
    phone: str
    email: str
