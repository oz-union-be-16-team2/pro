import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(".env.dev")  # 개발용. 배포면 .env로 바꾸거나 로직화

class Settings(BaseSettings):
    database_url: str

settings = Settings()