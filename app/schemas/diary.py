from pydantic import BaseModel
from datetime import datetime


class DiaryCreate(BaseModel):
    title: str
    content: str


class DiaryUpdate(BaseModel):
    title: str
    content: str


class DiaryResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


# ✅ A안: page/size 기반으로 변경 (limit/offset 제거)
class DiaryListResponse(BaseModel):
    data: list[DiaryResponse]
    page: int
    size: int
    total: int
    total_pages: int
