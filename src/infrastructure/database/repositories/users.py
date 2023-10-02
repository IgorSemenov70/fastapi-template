from uuid import UUID

from src.application.users.dto import User
from src.application.users.interfaces.persistence import UserRepository

from ..exception_mapper import exception_mapper
from .base import SQLAlchemyRepository


class UserRepositoryImpl(SQLAlchemyRepository, UserRepository):
    @exception_mapper
    async def get_by_id(self, user_id: UUID) -> User | None:
        return await self._session.get(User, user_id)
