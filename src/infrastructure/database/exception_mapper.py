from collections.abc import Callable
from functools import wraps
from typing import Any, Coroutine, ParamSpec, TypeVar

from sqlalchemy.exc import SQLAlchemyError

from src.application.common.exceptions import RepoError

Param = ParamSpec("Param")
ReturnType = TypeVar("ReturnType")
Func = Callable[Param, ReturnType]


def exception_mapper(
    func: Callable[Param, Coroutine[Any, Any, ReturnType]]
) -> Callable[Param, Coroutine[Any, Any, ReturnType]]:
    """
    Decorator to map SQLAlchemy errors to custom repository errors.

    This decorator is used to catch SQLAlchemy errors raised by a function and
    convert them into custom repository-related errors (RepoError). It wraps the
    provided function with error handling.
    """

    @wraps(func)
    async def wrapped(*args: Param.args, **kwargs: Param.kwargs) -> ReturnType:
        try:
            return await func(*args, **kwargs)
        except SQLAlchemyError as err:
            raise RepoError from err

    return wrapped
