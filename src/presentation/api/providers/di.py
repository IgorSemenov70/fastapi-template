from typing import AsyncGenerator, Annotated

from di import ScopeState, Container
from di.api.executor import SupportsAsyncExecutor
from fastapi import Depends

from src.infrastructure.di import DiScope


def get_di_container() -> Container:
    raise NotImplementedError


def get_di_executor() -> SupportsAsyncExecutor:
    raise NotImplementedError


def get_di_state() -> ScopeState:
    raise NotImplementedError


class StateProvider:
    def __init__(self, di_state: ScopeState | None = None) -> None:
        self._di_state = di_state

    async def build(
        self,
        container: Annotated[Container, Depends(get_di_container)],
    ) -> AsyncGenerator[ScopeState, None]:
        async with container.enter_scope(DiScope.REQUEST, self._di_state) as di_state:
            yield di_state
