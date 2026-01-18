import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from core.database import Base
from models.base import TimestampMixin


class AppointmentLog(Base, TimestampMixin):
    __tablename__ = "appointment_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    appointment_id = Column(UUID(as_uuid=True), ForeignKey("appointments.id"))
    previous_status_id = Column(
        UUID(as_uuid=True), ForeignKey("appointment_status.id"))
    new_status_id = Column(
        UUID(as_uuid=True), ForeignKey("appointment_status.id"))
    changed_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    change_reason = Column(String(255))
