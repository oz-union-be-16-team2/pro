from fastapi import APIRouter, Depends, HTTPException, Query

from app.dependencies.auth import get_current_user  # 너희 실제 경로 유지
from app.repositories.diary_repo import DiaryRepository
from app.schemas.diary import (
    DiaryCreate,
    DiaryUpdate,
    DiaryResponse,
    DiaryListResponse,
)

router = APIRouter(prefix="/diaries", tags=["Diary"])
repo = DiaryRepository()


# ✅ 생성
@router.post("/", response_model=DiaryResponse)
async def create_diary(
    data: DiaryCreate,
    current_user=Depends(get_current_user),
):
    return await repo.create(user_id=current_user.id, data=data)


# ✅ 내 일기 목록 (pagination)  ← 네가 만든 핵심 기능
@router.get("/me", response_model=DiaryListResponse)
async def list_my_diaries(
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    current_user=Depends(get_current_user),
):
    
    calculated_offset = (page - 1) * size

    data, total = await repo.list_by_user(
        user_id=current_user.id,
        limit=size,            
        offset=calculated_offset,
    )

    return {
        "data": data,
        "page": page,
        "size": size,
        "total": total,
        "total_pages": (total + size - 1) // size 
    }


# ✅ 내 일기 단건 조회 (선택이지만 거의 필수)
@router.get("/{diary_id}", response_model=DiaryResponse)
async def get_my_diary(
    diary_id: int,
    current_user=Depends(get_current_user),
):
    diary = await repo.get_by_id_and_user(diary_id=diary_id, user_id=current_user.id)
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")
    return diary


# ✅ 수정
@router.put("/{diary_id}", response_model=DiaryResponse)
async def update_diary(
    diary_id: int,
    data: DiaryUpdate,
    current_user=Depends(get_current_user),
):
    diary = await repo.get_by_id_and_user(diary_id=diary_id, user_id=current_user.id)
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")
    return await repo.update(diary=diary, data=data)


# ✅ 삭제
@router.delete("/{diary_id}")
async def delete_diary(
    diary_id: int,
    current_user=Depends(get_current_user),
):
    diary = await repo.get_by_id_and_user(diary_id=diary_id, user_id=current_user.id)
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")
    await repo.delete(diary=diary)
    return {"Diary was deleted": True}