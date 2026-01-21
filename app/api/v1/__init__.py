from fastapi import APIRouter

from .auth import router as auth_router
from .diary import router as diary_router
from .question import router as question_router
from .quote import router as quote_router

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(auth_router)
v1_router.include_router(diary_router)
v1_router.include_router(question_router)
v1_router.include_router(quote_router)
