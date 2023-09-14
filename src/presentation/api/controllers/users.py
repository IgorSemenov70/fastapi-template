from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status

from src.application.users.exceptions import UserNotFoundError
from src.application.users.interactors import GetUserById
from src.presentation.api.controllers.requests import UserResponse
from src.presentation.api.controllers.responses import ErrorResult
from src.presentation.api.providers import Stub

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@user_router.get(
    "/{user_id}",
    responses={
        status.HTTP_200_OK: {"model": UserResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[UserNotFoundError]},
    },
)
async def get_user_by_id_controller(
    user_id: UUID,
    interactor: Annotated[GetUserById, Depends(Stub(GetUserById))],
) -> UserResponse:
    user = await interactor(user_id=user_id)
    return UserResponse(id=user_id, username=user.username)
