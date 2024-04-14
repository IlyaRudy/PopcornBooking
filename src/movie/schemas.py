from datetime import datetime
from pydantic import BaseModel

# from src.movie_session.models import MovieSession


class MovieBase(BaseModel):
    title: str
    description: str
    duration: int


class MovieCreate(MovieBase):
    pass


class MovieRead(MovieBase):
    id: int
    # movie_session: MovieSession

    class Config:
        from_attributes = True


class MovieUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    duration: int | None = None
