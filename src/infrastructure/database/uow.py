from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.exceptions import CommitError, RollbackError
from src.application.common.interfaces import UnitOfWork


class SQLAlchemyUoW(UnitOfWork):
    """
    Unit of Work implementation using SQLAlchemy for asynchronous database operations.
    This class provides methods to commit and rollback transactions using an
    SQLAlchemy AsyncSession.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        """Commits the current transaction."""
        try:
            await self._session.commit()
        except SQLAlchemyError as err:
            raise CommitError from err

    async def rollback(self) -> None:
        """Rolls back the current transaction and discards changes."""
        try:
            await self._session.rollback()
        except SQLAlchemyError as err:
            raise RollbackError from err
