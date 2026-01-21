import os
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI
from tortoise import Tortoise
from dotenv import load_dotenv

from app.api.v1 import v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv(".env.dev")
    load_dotenv(".env")

    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL is not set. Check .env.dev/.env")

    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["app.models"]},
    )
    yield
    await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)
app.include_router(v1_router)
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")