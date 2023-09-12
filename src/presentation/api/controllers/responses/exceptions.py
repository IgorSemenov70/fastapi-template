from dataclasses import dataclass
from typing import Generic, TypeVar

from pydantic import BaseModel

TData = TypeVar("TData")


@dataclass(frozen=True)
class ErrorResult(BaseModel, Generic[TData]):
    """
    Class for representing an error result.

    This class provides a structure for holding information about error results,
    including an error message text and possibly associated data.
    """

    error: str
    data: TData
