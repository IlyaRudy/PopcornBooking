import sys


sys.path[0] = "/home/ilyarudy/my_projects/PopcornBooking"
from datetime import datetime
import random
from faker import Faker
from src.utils.demo_user_create import create_user
from src.database import async_session_maker
from src.book.models import Booking
from src.book.schemas import BookingCreate
from src.movie_session.models import MovieSession
from src.movie.models import Movie
from src.movie.schemas import MovieCreate
from src.cinema.models import Cinema
from src.cinema.schemas import CinemaCreate
from src.auth.models import User
from src.auth.schemas import UserCreate
from src.movie_session.schemas import MovieSessionCreate
from sqlalchemy.ext.asyncio import AsyncSession


async def create_demo_data(num_entries: int):
    async with async_session_maker() as session:
        session: AsyncSession
        fake: Faker = Faker()

        for _ in range(num_entries):
            password = fake.password()
            user_data = await create_user(
                username=fake.user_name(),
                fullname=fake.name(),
                password=password,
                email=fake.email(),
                phone_number=fake.phone_number(),
            )
            with open("demo_users_data.txt", "a") as file:
                file.write(f"Email: {user_data.email} , Password: {password}\n")

            cinema_data = CinemaCreate(
                name=fake.name(),
                city=fake.city(),
                address=fake.address().replace("\n", " "),
            )
            movie_data = MovieCreate(
                title=fake.sentence(),
                description=fake.text(),
                duration=random.randint(60, 180),
            )
            cinema = Cinema(**cinema_data.model_dump())
            movie = Movie(**movie_data.model_dump())
            session.add(cinema)
            session.add(movie)
            await session.commit()

            movie_session_data = MovieSessionCreate(
                movie_id=movie.id,
                cinema_id=cinema.id,
                start_time=fake.date_time_this_year(),
            )
            movie_session = MovieSession(**movie_session_data.model_dump())
            session.add(movie_session)
            await session.commit()

            booking_data = BookingCreate(
                user_id=user_data.id,
                movie_session_id=movie_session.id,
                booked_seats=random.randint(1, 500),
                booking_time=datetime.now(),
                status="booked",
            )
            booking = Booking(**booking_data.model_dump())
            session.add(booking)
            await session.commit()


if __name__ == "__main__":
    import asyncio

    asyncio.run(create_demo_data(num_entries=100))
