from di import Container, ScopeState
from di.api.executor import SupportsAsyncExecutor

from fastapi import FastAPI

from src.application.users.interactors import GetUserById

from .build_interactors import build_get_user_by_id_interactor
from .di import StateProvider, get_di_container, get_di_executor, get_di_state
from .stub import Stub


def init_providers(
    app: FastAPI,
    di_executor: SupportsAsyncExecutor,
    di_container: Container,
    di_state: ScopeState | None = None,
) -> None:
    state_provider = StateProvider(di_state)
    app.dependency_overrides[get_di_container] = lambda: di_container
    app.dependency_overrides[get_di_executor] = lambda: di_executor
    app.dependency_overrides[get_di_state] = state_provider.build
    app.dependency_overrides[Stub(GetUserById)] = build_get_user_by_id_interactor
