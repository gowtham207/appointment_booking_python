import uuid
from sqlalchemy import Column, Text, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from models.base import TimestampMixin


class Appointment(Base, TimestampMixin):
    __tablename__ = "appointments"
    __table_args__ = (
        UniqueConstraint("slot_id"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"))
    physician_id = Column(UUID(as_uuid=True), ForeignKey("physicians.id"))
    location_id = Column(UUID(as_uuid=True), ForeignKey("locations.id"))
    slot_id = Column(UUID(as_uuid=True), ForeignKey("slots.id"))
    status_id = Column(UUID(as_uuid=True), ForeignKey("appointment_status.id"))
    booked_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    org_id = Column(UUID(as_uuid=True), ForeignKey(
        "organizations.id"), nullable=False)

    notes = Column(Text)

    status = relationship("AppointmentStatus")
