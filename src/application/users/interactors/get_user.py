from uuid import UUID

from ...common.interactor import Interactor
from ..dto import User
from ..exceptions import UserNotFoundError
from ..interfaces.persistence import UserRepository


class GetUserById(Interactor[UUID, User]):
    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo

    async def __call__(self, user_id: UUID) -> User:
        user = await self._user_repo.get_by_id(user_id=user_id)
        if user is None:
            raise UserNotFoundError(user_id)
        return user
