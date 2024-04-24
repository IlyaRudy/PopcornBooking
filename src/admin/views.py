from sqladmin import ModelView

from src.auth.models import User
from src.book.models import Booking
from src.cinema.models import Cinema
from src.movie.models import Movie
from src.movie_session.models import MovieSession


class UserAdmin(ModelView, model=User):
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"
    category = "Accounts"

    column_list = [
        User.username,
        User.email,
        User.fullname,
        User.phone_number,
        User.bookings,
    ]
    column_details_exclude_list = [
        User.id,
        User.hashed_password,
    ]
    form_include_pk = False
    can_delete = False
    can_create = False
    can_view_details = True


class BookingAdmin(ModelView, model=Booking):
    name = "Booking"
    name_plural = "Bookings"
    icon = "fa-solid fa-ticket"
    category = "Booking"

    column_list = [
        Booking.id,
        Booking.user,
        Booking.movie_session,
        Booking.booked_seats,
        Booking.booking_time,
        Booking.status,
    ]
    column_details_exclude_list = [
        Booking.id,
        Booking.user_id,
        Booking.movie_session_id,
    ]
    form_include_pk = False


class MovieSessionAdmin(ModelView, model=MovieSession):

    name = "Movie session"
    name_plural = "Movie sessions"
    icon = "fa-solid fa-calendar-check"
    category = "Booking"

    column_list = [
        MovieSession.id,
        MovieSession.cinema,
        MovieSession.movie,
        MovieSession.start_time,
    ]


class CinemaAdmin(ModelView, model=Cinema):
    name = "Cinema"
    name_plural = "Cinemas"
    icon = "fa-solid fa-arrow-right-to-city"
    category = "Booking"

    column_list = [
        Cinema.name,
        Cinema.city,
        Cinema.movie_session,
    ]


class MovieAdmin(ModelView, model=Movie):
    name = "Movie"
    name_plural = "Movies"
    icon = "fa-solid fa-film"
    category = "Booking"

    column_list = [
        Movie.title,
        Movie.duration,
        Movie.movie_session,
    ]
