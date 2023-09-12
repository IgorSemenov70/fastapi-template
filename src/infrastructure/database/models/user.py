import sqlalchemy as sa
from uuid6 import uuid7

from src.application.users.dto import User
from .base import mapper_registry


user_table = sa.Table(
    "users",
    mapper_registry.metadata,
    sa.Column(
        "id",
        sa.Uuid(),
        primary_key=True,
        default=uuid7,
        server_default=sa.func.uuid_generate_v7(),
        index=True,
    ),
    sa.Column("username", sa.String(), unique=True),
    sa.Column("first_name", sa.String(), nullable=False),
    sa.Column("last_name", sa.String(), nullable=False),
    sa.Column("middle_name", sa.String(), nullable=False),
    sa.Column("deleted", sa.Boolean(), default=False, server_default=sa.False_(), nullable=False),
    sa.Column(
        "created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()
    ),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.func.now(),
        onupdate=sa.func.now(),
    ),
)

mapper_registry.map_imperatively(User, user_table)
