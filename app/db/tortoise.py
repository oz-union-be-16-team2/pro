# app/db/tortoise.py
import os
from tortoise.contrib.fastapi import register_tortoise
from dotenv import load_dotenv

def init_tortoise(app):
    # .env.dev 우선 로드 (없으면 .env)
    load_dotenv(".env.dev")
    load_dotenv(".env")

    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL is not set. Check your .env.dev or .env")

    register_tortoise(
        app,
        db_url=db_url,
        modules={"models": ["app.models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
