from di import Container, bind_by_type
from di.api.scopes import Scope
from di.dependent import Dependent
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.application.common.interfaces import UnitOfWork
from src.application.users.interactors import GetUserById
from src.application.users.interfaces.persistence import UserRepository
from src.infrastructure.database.main import (
    build_sa_engine,
    build_sa_session,
    build_sa_session_factory,
)
from src.infrastructure.database.repositories.users import UserRepositoryImpl
from src.infrastructure.database.uow import SQLAlchemyUoW
from src.infrastructure.di import DiScope


def init_di_container(di_container: Container) -> None:
    di_container.bind(bind_by_type(Dependent(build_sa_engine, scope=DiScope.APP), AsyncEngine))
    di_container.bind(
        bind_by_type(
            Dependent(build_sa_session_factory, scope=DiScope.APP),
            async_sessionmaker[AsyncSession],
        )
    )
    di_container.bind(
        bind_by_type(Dependent(build_sa_session, scope=DiScope.REQUEST), AsyncSession)
    )
    di_container.bind(
        bind_by_type(Dependent(SQLAlchemyUoW, scope=DiScope.REQUEST), UnitOfWork, covariant=True)
    )
    _setup_database_repositories(di_container=di_container, scope=DiScope.REQUEST)
    _setup_application_handlers(di_container=di_container, scope=DiScope.REQUEST)


def _setup_database_repositories(di_container: Container, scope: Scope) -> None:
    di_container.bind(
        bind_by_type(Dependent(UserRepositoryImpl, scope=scope), UserRepository, covariant=True)
    )


def _setup_application_handlers(di_container: Container, scope: Scope) -> None:
    di_container.bind(bind_by_type(Dependent(GetUserById, scope=scope), GetUserById))
