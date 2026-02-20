import uuid
from sqlalchemy import Column, Date, Time, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from models.base import TimestampMixin


class Slot(Base, TimestampMixin):
    __tablename__ = "slots"
    __table_args__ = (
        UniqueConstraint("physician_id", "location_id",
                         "slot_date", "start_time"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    physician_id = Column(UUID(as_uuid=True), ForeignKey("physicians.id"))
    location_id = Column(UUID(as_uuid=True), ForeignKey("locations.id"))

    slot_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    is_available = Column(Boolean, default=True)
    org_id = Column(UUID(as_uuid=True), ForeignKey(
        "organizations.id"), nullable=False)
    physician = relationship("Physician", back_populates="slots")
