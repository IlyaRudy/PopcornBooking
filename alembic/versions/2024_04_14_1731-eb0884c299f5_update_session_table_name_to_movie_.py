"""Update session table name to movie_session

Revision ID: eb0884c299f5
Revises: f074d107d0b4
Create Date: 2024-04-14 17:31:06.434017

"""

from typing import Sequence, Union

from alembic import op
import fastapi_users_db_sqlalchemy
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "eb0884c299f5"
down_revision: Union[str, None] = "f074d107d0b4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "movie_session",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column("cinema_id", sa.Integer(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["cinema_id"],
            ["cinema.id"],
        ),
        sa.ForeignKeyConstraint(
            ["movie_id"],
            ["movie.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_movie_session_id"), "movie_session", ["id"], unique=False)
    op.create_table(
        "booking",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "user_id",
            fastapi_users_db_sqlalchemy.generics.GUID(),
            nullable=False,
        ),
        sa.Column("movie_session_id", sa.Integer(), nullable=False),
        sa.Column("booked_seats", sa.Integer(), nullable=False),
        sa.Column(
            "booking_time",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("status", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["movie_session_id"],
            ["movie_session.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_booking_id"), "booking", ["id"], unique=False)
    op.drop_index("ix_bookings_id", table_name="bookings")
    op.drop_table("bookings")
    op.drop_index("ix_session_id", table_name="session")
    op.drop_table("session")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "session",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('session_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("movie_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "start_time",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("cinema_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["cinema_id"], ["cinema.id"], name="session_cinema_id_fkey"
        ),
        sa.ForeignKeyConstraint(
            ["movie_id"], ["movie.id"], name="session_movie_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="session_pkey"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("ix_session_id", "session", ["id"], unique=False)
    op.create_table(
        "bookings",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("session_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("booked_seats", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "booking_time",
            postgresql.TIMESTAMP(),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("status", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["session_id"], ["session.id"], name="bookings_session_id_fkey"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], name="bookings_user_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="bookings_pkey"),
    )
    op.create_index("ix_bookings_id", "bookings", ["id"], unique=False)
    op.drop_index(op.f("ix_booking_id"), table_name="booking")
    op.drop_table("booking")
    op.drop_index(op.f("ix_movie_session_id"), table_name="movie_session")
    op.drop_table("movie_session")
    # ### end Alembic commands ###
