from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # ✅ 이 줄 추가
    )


    # DB
    DATABASE_URL: str

    # 기존 보안 키 (이미 있으면 유지)
    SECRET_KEY: str

    # ✅ JWT 관련 (추가)
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60

settings = Settings()

