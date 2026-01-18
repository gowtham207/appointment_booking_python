import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from core.database import Base
from models.base import TimestampMixin


class AppointmentStatus(Base, TimestampMixin):
    __tablename__ = "appointment_status"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(String(50), unique=True, nullable=False)
    description = Column(String(150))
