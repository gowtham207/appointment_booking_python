import enum


class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    PHYSICIAN = "PHYSICIAN"
    PATIENT = "PATIENT"
    STAFF = "STAFF"


class Gender(str, enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
