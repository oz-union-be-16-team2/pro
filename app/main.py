from fastapi import FastAPI
from app.db.tortoise import init_tortoise

app = FastAPI()

init_tortoise(app)