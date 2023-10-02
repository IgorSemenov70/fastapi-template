from typing import Annotated

from di import Container, ScopeState
from di.api.executor import SupportsAsyncExecutor
from di.dependent import Dependent

from fastapi import Depends

from src.application.users.interactors import GetUserById
from src.infrastructure.di import DiScope

from ..di import get_di_container, get_di_executor, get_di_state


async def build_get_user_by_id_interactor(
    di_container: Annotated[Container, Depends(get_di_container)],
    di_executor: Annotated[SupportsAsyncExecutor, Depends(get_di_executor)],
    di_state: Annotated[ScopeState, Depends(get_di_state)],
) -> GetUserById:
    solved_dependency = di_container.solve(Dependent(GetUserById), [DiScope.APP, DiScope.REQUEST])
    return await solved_dependency.execute_async(executor=di_executor, state=di_state)
