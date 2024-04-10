from sqlalchemy import Column, String, Boolean, DateTime, Date
from sqlalchemy.sql import func
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from src.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    email = Column(String, unique=True, nullable=False, index=True)
    username = Column(String, nullable=False, unique=True, index=True)
    fullname = Column(String)
    registered_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    phone_number = Column(String)
