import sys

sys.path[0] = "/home/ilyarudy/my_projects/PopcornBooking"
import contextlib

from pydantic import EmailStr

from src.auth.utils import get_user_db
from src.database import get_async_session
from src.auth.schemas import UserCreate
from src.auth.manager import get_user_manager
from fastapi_users.exceptions import UserAlreadyExists

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
    username: str,
    email: EmailStr,
    password: str,
    is_superuser: bool = False,
    fullname: str | None = None,
    phone_number: str | None = None,
):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        UserCreate(
                            username=username,
                            email=email,
                            password=password,
                            is_superuser=is_superuser,
                            fullname=fullname,
                            phone_number=phone_number,
                        )
                    )
                    print(f"User created {user}")
                    return user
    except UserAlreadyExists:
        print(f"User {email} already exists")
        raise
