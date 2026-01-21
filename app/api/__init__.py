from fastapi import APIRouter
from app.api.v1 import v1_router
from app.api.v1.users import router as users_router

v1_router.include_router(users_router)
api_router = APIRouter()
api_router.include_router(v1_router, prefix="/v1")
