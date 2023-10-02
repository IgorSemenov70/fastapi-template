from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from di import Container
from di.executors import AsyncExecutor

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.infrastructure.di import DiScope, init_di_container
from src.presentation.api.controllers import init_controllers, init_exception_handlers
from src.presentation.api.middlewares import init_middlewares
from src.presentation.api.providers import init_providers


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    di_container = Container()
    di_executor = AsyncExecutor()
    init_di_container(di_container=di_container)
    async with di_container.enter_scope(scope=DiScope.APP) as di_state:
        init_providers(app, di_container=di_container, di_executor=di_executor, di_state=di_state)
        init_controllers(app)
        yield


def create_app() -> FastAPI:
    app = FastAPI(default_response_class=ORJSONResponse, lifespan=lifespan)
    init_middlewares(app)
    init_exception_handlers(app)
    return app


if __name__ == "__main__":
    uvicorn.run(create_app, factory=True, host="0.0.0.0", port=8000)
