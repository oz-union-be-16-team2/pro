from tortoise.contrib.fastapi import RegisterTortoise
from app.database import TORTOISE_ORM

def init_db(app):
    """
    FastAPI app에 Tortoise ORM 등록
    """
    RegisterTortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,  # 배포에서는 False, 개발 시 True 가능
        add_exception_handlers=True,
    )