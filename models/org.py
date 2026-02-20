from core.database import Base
from models.base import TimestampMixin
from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.dialects.postgresql import UUID


class Organization(Base, TimestampMixin):
    __tablename__ = "organizations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    website = Column(String(255))
    contact_email = Column(String(255))
    contact_phone = Column(String(20))
    address = Column(Text)
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))
    postal_code = Column(String(20))
