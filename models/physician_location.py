import uuid
from sqlalchemy import Column, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from models.base import TimestampMixin


class PhysicianLocation(Base, TimestampMixin):
    __tablename__ = "physician_locations"
    __table_args__ = (
        UniqueConstraint("physician_id", "location_id"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    physician_id = Column(UUID(as_uuid=True), ForeignKey("physicians.id"))
    location_id = Column(UUID(as_uuid=True), ForeignKey("locations.id"))
    is_active = Column(Boolean, default=True)

    physician = relationship("Physician", back_populates="locations")
    location = relationship("Location", back_populates="physicians")
