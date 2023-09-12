from pydantic import BaseModel

from fastapi import APIRouter, status

healthcheck_router = APIRouter(
    prefix="/healthcheck",
    tags=["healthcheck"],
)


class OkStatus(BaseModel):
    status: str = "ok"


@healthcheck_router.get("/", status_code=status.HTTP_200_OK)
async def healthcheck_handler() -> OkStatus:
    """Returns a status indicating the health of the application."""
    return OkStatus()
