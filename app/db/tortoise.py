from tortoise.contrib.fastapi import register_tortoise
from app.core.config import settings

def init_tortoise(app):
    register_tortoise(
        app,
        db_url=settings.database_url,
        modules={"models": ["app.models.user", "app.models.diary", "app.models.quote", "app.models.question"]},
        generate_schemas=False,  # 운영에서는 False 권장 (마이그레이션 사용)
        add_exception_handlers=True,
    )
