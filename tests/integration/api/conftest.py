from typing import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import AsyncClient

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.presentation.api.controllers.routers import init_controllers


@pytest.fixture(scope="session")
def app() -> FastAPI:
    app = FastAPI(default_response_class=ORJSONResponse)
    init_controllers(app)
    return app


@pytest.mark.anyio()
@pytest_asyncio.fixture(scope="session")
async def client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
