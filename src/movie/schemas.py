from datetime import datetime
from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    description: str | None
    duration: int


class MovieCreate(MovieBase):
    pass


class MovieRead(MovieBase):
    id: int
    session: list[dict]

    class Config:
        from_attributes = True


class MovieUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    duration: int | None = None
