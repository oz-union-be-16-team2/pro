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
        

class DiaryListResponse(BaseModel):
    data: list[DiaryResponse]
    limit: int
    offset: int
    total: int