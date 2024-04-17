from src.book.schemas import BookingRead as BookingReadParent
from src.cinema.schemas import CinemaRead
from src.movie.schemas import MovieRead
from src.movie_session.schemas import MovieSessionBase


class MovieSessionToBooking(MovieSessionBase):
    id: int
    movie: MovieRead
    cinema: CinemaRead


class BookingRead(BookingReadParent):
    movie_session: "MovieSessionToBooking"
