from fastapi import FastAPI
from src.admin.views import (
    BookingAdmin,
    CinemaAdmin,
    MovieAdmin,
    MovieSessionAdmin,
    UserAdmin,
)
from src.auth.router import auth_router
from src.cinema.router import cinema_router
from src.movie.router import movie_router
from src.movie_session.router import movie_session_router
from src.book.router import booking_router

from sqladmin import Admin
from src.database import async_engine


app = FastAPI(title="PopcornBooking")

app.include_router(auth_router)
app.include_router(cinema_router)
app.include_router(movie_router)
app.include_router(movie_session_router)
app.include_router(booking_router)


admin = Admin(app, async_engine)

admin.add_view(UserAdmin)
admin.add_view(BookingAdmin)
admin.add_view(MovieSessionAdmin)
admin.add_view(CinemaAdmin)
admin.add_view(MovieAdmin)
