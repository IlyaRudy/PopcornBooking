from datetime import date
from uuid import UUID
from fastapi_users import schemas
from pydantic import BaseModel, EmailStr


class UserRead(schemas.BaseUser[UUID]):
    id: UUID
    email: str
    username: str | None
    fullname: str | None
    phone_number: str | None
    date_of_birth: date | None
    profile_picture_url: str | None


class UserCreate(schemas.BaseUserCreate):
    username: str
    fullname: str | None
    phone_number: str | None
    date_of_birth: date | None


class UserUpdate(schemas.BaseUserUpdate):
    username: str | None
    fullname: str | None
    phone_number: str | None
    date_of_birth: date | None
    profile_picture_url: str | None
