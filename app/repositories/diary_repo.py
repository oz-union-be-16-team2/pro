from app.models.diary import Diary
from app.schemas.diary import DiaryCreate, DiaryUpdate


class DiaryRepository:
    async def create(self, user_id: int, data: DiaryCreate) -> Diary:
        return await Diary.create(
            title=data.title,
            content=data.content,
            users_id=user_id,
        )

    async def get_by_id(self, diary_id: int) -> Diary | None:
        return await Diary.filter(id=diary_id).first()

    async def get_by_user(self, user_id: int) -> list[Diary]:
        return await Diary.filter(users_id=user_id).all()

    async def get_by_id_and_user(self, diary_id: int, user_id: int) -> Diary | None:
        return await Diary.filter(id=diary_id, users_id=user_id).first()

    # ✅ 추가: 내 일기 목록 pagination
    async def list_by_user(
        self,
        user_id: int,
        limit: int = 20,
        offset: int = 0,
    ) -> tuple[list[Diary], int]:
        base = Diary.filter(users_id=user_id).order_by("-id")  # 최신 먼저
        total = await base.count()
        data = await base.limit(limit).offset(offset)
        return data, total

    async def update(self, diary: Diary, data: DiaryUpdate) -> Diary:
        diary.title = data.title
        diary.content = data.content
        await diary.save()
        return diary

    async def delete(self, diary: Diary) -> None:
        await diary.delete()
