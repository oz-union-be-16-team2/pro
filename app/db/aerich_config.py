from tortoise import Tortoise
from app.core.config import settings  # ⚠️ 네 프로젝트 설정 경로에 맞게 조정

TORTOISE_ORM = {
    "connections": {
        "default": settings.database_url,
    },
    "apps": {
        "models": {
            # ⚠️ 여기 진짜 중요
            # app.models.__init__ 안에 import된 모델만 aerich가 인식함
            "models": [
                "app.models",
                "aerich.models",
            ],
            "default_connection": "default",
        },
    },
}
