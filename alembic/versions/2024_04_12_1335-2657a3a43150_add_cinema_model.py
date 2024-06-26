"""add cinema model

Revision ID: 2657a3a43150
Revises: ca51ac0a8836
Create Date: 2024-04-12 13:35:54.230913

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2657a3a43150"
down_revision: Union[str, None] = "ca51ac0a8836"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cinema",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=True),
        sa.Column("city_district", sa.String(), nullable=True),
        sa.Column("addres", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_cinema_id"), "cinema", ["id"], unique=False)
    op.add_column(
        "session", sa.Column("cinema_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key(None, "session", "cinema", ["cinema_id"], ["id"])
    op.drop_column("session", "room_number")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "session",
        sa.Column(
            "room_number", sa.VARCHAR(), autoincrement=False, nullable=False
        ),
    )
    op.drop_constraint(None, "session", type_="foreignkey")
    op.drop_column("session", "cinema_id")
    op.drop_index(op.f("ix_cinema_id"), table_name="cinema")
    op.drop_table("cinema")
    # ### end Alembic commands ###
