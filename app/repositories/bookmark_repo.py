# app/repositories/bookmark_repo.py
from app.models.bookmark import Bookmark

class BookmarkRepository:

    async def add(self, user_id: int, quote_id: int):
        await Bookmark.get_or_create(
            user_id=user_id,
            quote_id=quote_id,
        )

    async def list_by_user(self, user_id: int):
        return await Bookmark.filter(user_id=user_id).prefetch_related("quote")

    async def remove(self, user_id: int, quote_id: int):
        bookmark = await Bookmark.filter(
            user_id=user_id,
            quote_id=quote_id,
        ).first()
        if bookmark:
            await bookmark.delete()