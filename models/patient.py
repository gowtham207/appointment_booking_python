import uuid
from sqlalchemy import Column, String, Date, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from models.base import TimestampMixin
from models.enum import Gender


class Patient(Base, TimestampMixin):
    __tablename__ = "patients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    full_name = Column(String(150), nullable=False)
    dob = Column(Date)
    gender = Column(Enum(Gender))
    phone = Column(String(20))
    email = Column(String(150))

    user = relationship("User", back_populates="patient")
