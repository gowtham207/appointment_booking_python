import uuid
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from models.base import TimestampMixin


class Location(Base, TimestampMixin):
    __tablename__ = "locations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(150), nullable=False)
    address = Column(Text)
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))
    postal_code = Column(String(20))
    org_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)


    physicians = relationship("PhysicianLocation", back_populates="location")
