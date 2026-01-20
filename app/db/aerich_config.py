from app.core.config import settings

TORTOISE_ORM = {
    "connections": {
        "default": settings.database_url,  # .env.dev의 DATABASE_URL을 읽어야 함
    },
    "apps": {
        "models": {
            "models": [
                "app.models.user",
                "app.models.diary",
                "app.models.quote",
                "app.models.question",
                "aerich.models",
            ],
            "default_connection": "default",
        }
    },
}
