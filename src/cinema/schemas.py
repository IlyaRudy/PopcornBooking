from pydantic import BaseModel


class CinemaBase(BaseModel):
    name: str
    city: str | None = None
    city_district: str | None = None
    address: str | None = None


class CinemaCreate(CinemaBase):
    pass


class CinemaRead(CinemaBase):
    id: int

    class Config:
        orm_mode = True


class CinemaUpdate(BaseModel):
    name: str | None = None
    city: str | None = None
    city_district: str | None = None
    address: str | None = None
