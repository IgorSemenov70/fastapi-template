from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from src.application.users.interactors import GetUserById
from src.presentation.api.controllers.requests.users import UserResponse
from src.presentation.api.providers import Stub

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@user_router.get("/{user_id:uuid}", response_model=UserResponse)
async def get_user_by_id_controller(
    user_id: UUID,
    interactor: Annotated[GetUserById, Depends(Stub(GetUserById))],
):
    return await interactor(user_id=user_id)
