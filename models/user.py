import uuid
from sqlalchemy import Column, String, Boolean, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.database import Base
from models.base import TimestampMixin
from models.enum import UserRole, Gender


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role = Column(Enum(UserRole), nullable=False)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    phone = Column(String(20))
    password_hash = Column(String(255))
    is_active = Column(Boolean, default=True)
    mfa_hash = Column(String(255), default=None)
    gender = Column(Enum(Gender))
    mfa_enabled = Column(Boolean, default=False)
    last_login = Column(DateTime, nullable=True, server_default=func.now())

    physician = relationship("Physician", back_populates="user", uselist=False)
    patient = relationship("Patient", back_populates="user", uselist=False)
