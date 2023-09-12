import logging

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette import status
from starlette.requests import Request

from src.application.common.exceptions import ApplicationError
from src.application.users.exceptions import UserNotFoundError
from .responses import ErrorResult

logger = logging.getLogger(__name__)


def setup_exception_handlers(app: FastAPI) -> None:
    """
    Set up custom exception handlers for a FastAPI application.
    This function registers a custom exception handler for the specified FastAPI
    application.
    """
    app.add_exception_handler(UserNotFoundError, user_not_found_handler)
    app.add_exception_handler(Exception, unknown_exception_handler)


async def user_not_found_handler(request: Request, err: UserNotFoundError) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_404_NOT_FOUND)


async def unknown_exception_handler(_: Request, err: Exception) -> ORJSONResponse:
    """Custom exception handler for handling unknown exceptions."""
    logger.error("Handle error", exc_info=err, extra={"error": err})
    logger.exception("Unknown error occurred", exc_info=err, extra={"error": err})
    return ORJSONResponse(
        ErrorResult(error="Unknown server error has occurred", data=err),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


async def handle_error(
    _: Request, err: ApplicationError, status_code: int
) -> ORJSONResponse:
    """Custom error handler for handling known application errors."""
    logger.error("Handle error", exc_info=err, extra={"error": err})
    return ORJSONResponse(
        ErrorResult(error=err.message, data=err),
        status_code=status_code,
    )
