# app/api/v1/bookmark.py
from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.auth import get_current_user
from app.repositories.bookmark_repo import BookmarkRepository

router = APIRouter(prefix="/bookmarks", tags=["Bookmarks"])
repo = BookmarkRepository()


@router.post("/{quote_id}")
async def add_bookmark(
    quote_id: int,
    current_user=Depends(get_current_user),
):
    await repo.add(user_id=current_user.id, quote_id=quote_id)
    return {"ok": True}


@router.get("/me")
async def list_my_bookmarks(
    current_user=Depends(get_current_user),
):
    return await repo.list_by_user(current_user.id)


@router.delete("/{quote_id}")
async def remove_bookmark(
    quote_id: int,
    current_user=Depends(get_current_user),
):
    await repo.remove(user_id=current_user.id, quote_id=quote_id)
    return {"ok": True}