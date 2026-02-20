import uuid
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from models.base import TimestampMixin


class Physician(Base, TimestampMixin):
    __tablename__ = "physicians"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True)

    specialization = Column(String(150))
    experience_years = Column(Integer)
    license_number = Column(String(100))
    org_id = Column(UUID(as_uuid=True), ForeignKey(
        "organizations.id"), nullable=False)
    user = relationship("User", back_populates="physician")
    locations = relationship("PhysicianLocation", back_populates="physician")
    slots = relationship("Slot", back_populates="physician")
