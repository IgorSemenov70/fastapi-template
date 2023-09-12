"""create_user_table

Revision ID: 3ca63286765c
Revises: a3c0c2c09683
Create Date: 2023-09-10 18:57:25.723244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3ca63286765c"
down_revision: Union[str, None] = "a3c0c2c09683"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Uuid(), server_default=sa.func.uuid_generate_v7(), nullable=False),
        sa.Column("username", sa.String(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("middle_name", sa.String(), nullable=False),
        sa.Column("deleted", sa.Boolean(), server_default=sa.False_(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("username", name=op.f("uq_users_username")),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
