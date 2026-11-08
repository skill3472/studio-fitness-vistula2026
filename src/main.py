import sys
from pathlib import Path

import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from auth.router import router as auth_router
from common.db.database import create_schema
from common.router import router as common_router
from config import settings

api_router = APIRouter(prefix="/api")
front_router = APIRouter(prefix="", tags=["Frontend"])

api_router.include_router(common_router, prefix="", tags=["Common"])
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_schema()
    yield

app = FastAPI(title="Vistula Fitness 2026", lifespan=lifespan)

app.include_router(api_router)
app.include_router(front_router)

@front_router.get("/")
def get_front() -> FileResponse:
    return FileResponse(
        path=(settings.FRONT_DIRECTORY / "index.html") 
    )


if __name__ == "__main__":
    # In production environments, run the app with uvicorn directly instead,
    # this is only for local debugger purposes.
    #
    # For example, in prod use:
    # > uv run uvicorn src.main:app
    # from app root.
    uvicorn.run(app, host="127.0.0.1", port=8000)
