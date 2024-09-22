"""create user table

Revision ID: 48d821905984
Revises: 12dcd758c7ba
Create Date: 2024-09-22 12:05:33.916290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '48d821905984'
down_revision: Union[str, None] = '12dcd758c7ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def create_user_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("username", sa.String(20), nullable=False),
        sa.Column("email", sa.String(50), nullable=False, index=True),
        sa.Column("password", sa.String(300), nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )


def upgrade_engine1() -> None:
    create_user_table()


def downgrade_engine1() -> None:
    op.drop_table("users")


def upgrade_engine2() -> None:
    create_user_table()


def downgrade_engine2() -> None:
    op.drop_table("users")

