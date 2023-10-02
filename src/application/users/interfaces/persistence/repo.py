from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from src.application.users.dto import User


class UserRepository(Protocol):
    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> User | None:
        raise NotImplementedError
