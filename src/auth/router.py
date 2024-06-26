from fastapi import APIRouter
from src.auth.config import auth_backend, fastapi_users
from src.auth.schemas import UserCreate, UserRead


auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

auth_router.include_router(fastapi_users.get_auth_router(auth_backend))

auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))

auth_router.include_router(fastapi_users.get_reset_password_router())
