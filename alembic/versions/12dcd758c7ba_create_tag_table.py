"""create tag table

Revision ID: 12dcd758c7ba
Revises: 
Create Date: 2024-08-25 15:40:32.548844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '12dcd758c7ba'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()





def upgrade_engine1() -> None:
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(20), nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=func.now()),
        sa.Column("updated_at", sa.DateTime, server_default=func.now(), onupdate=func.now())
    )


def downgrade_engine1() -> None:
    op.drop_table("tags")


def upgrade_engine2() -> None:
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(20), nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=func.now()),
        sa.Column("updated_at", sa.DateTime, server_default=func.now(), onupdate=func.now())
    )


def downgrade_engine2() -> None:
    op.drop_table("tags")

