from fastapi import FastAPI

from .exceptions import setup_exception_handlers
from .healthcheck import healthcheck_router
from .users import user_router


def init_controllers(app: FastAPI) -> None:
    """Adds the defined routers and controllers to the FastAPI app."""
    app.include_router(healthcheck_router)
    app.include_router(user_router)
    # setup_exception_handlers(app)
