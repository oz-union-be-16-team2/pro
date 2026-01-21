# app/api/v1/users.py
from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
async def get_my_info(current_user: User = Depends(get_current_user)):
    # 그대로 유저 정보 반환
    return {
        "id": current_user.id,
        "username": current_user.username,
        "created_at": current_user.created_at,
    }


@router.get("/{user_id}")
async def get_user_detail(
    user_id: int,
    current_user: User = Depends(get_current_user),
):
    # 본인 정보만 조회 가능하게 막기
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access denied")

    return {
        "id": current_user.id,
        "username": current_user.username,
        "created_at": current_user.created_at,
    }