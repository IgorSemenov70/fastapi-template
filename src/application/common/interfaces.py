from abc import abstractmethod
from typing import Protocol


class UnitOfWork(Protocol):
    """
    Abstract base class for the Unit of Work pattern.

    This class defines the interface for managing transactions and provides
    methods for committing and rolling back a transaction.
    """

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError
