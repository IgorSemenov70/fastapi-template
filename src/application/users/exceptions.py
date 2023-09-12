from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions import ApplicationError


@dataclass(eq=False)
class UserNotFoundError(ApplicationError):
    user_id: UUID

    @property
    def message(self) -> str:
        return f'A user with "{self.user_id}" user_id not found'
